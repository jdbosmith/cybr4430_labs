import cmath
import math
import re
import numpy as np
import random

# ------------------------------------------------------------
# Basis states
# ------------------------------------------------------------

class Qubit:
    def __init__(self, a, b):
        self.a = complex(a)
        self.b = complex(b)

    # --------------------------------------------------------
    # Basic qubit properties
    # --------------------------------------------------------

    def norm(self):
        return abs(self.a)**2 + abs(self.b)**2

    def is_valid(self, tol=1e-12):
        return abs(self.norm() - 1) < tol
    
    def is_superposition(self, tol=1e-12):
        return abs(self.a) > tol and abs(self.b) > tol
    
    def inner(self, other):
        return (self.a.conjugate() * other.a +
                self.b.conjugate() * other.b)
    
    def probability_of(self, basis_state):
        amp = basis_state.inner(self)
        return abs(amp)**2

    # --------------------------------------------------------
    # Canonical form (remove global phase)
    # --------------------------------------------------------

    def canonical(self, tol=1e-12):
        a, b = self.a, self.b

        if abs(a) > tol:
            phase = a / abs(a)
        elif abs(b) > tol:
            phase = b / abs(b)
        else:
            return Qubit(0, 0)

        return Qubit(a / phase, b / phase)
    
    def canonical_pretty(self, digits=6):
        return self.canonical().pretty(digits)

    def pretty(self, digits=6):
        a = round(self.a.real, digits) + round(self.a.imag, digits)*1j
        b = round(self.b.real, digits) + round(self.b.imag, digits)*1j
        return f"Qubit(a={a}, b={b})"

    # --------------------------------------------------------
    # Apply a unitary gate
    # --------------------------------------------------------

    def apply_gate(self, U):
        a = U[0][0] * self.a + U[0][1] * self.b
        b = U[1][0] * self.a + U[1][1] * self.b
        return Qubit(a, b)

    # --------------------------------------------------------
    # Measurement
    # --------------------------------------------------------

    def measure(self, basis=None):
        if basis is None:
            basis = [ket0, ket1]

        amps = [b.inner(self) for b in basis]
        probs = [abs(a)**2 for a in amps]

        outcome = random.choices(range(len(basis)), weights=probs)[0]
        collapsed = basis[outcome]

        return outcome, collapsed, probs

    # --------------------------------------------------------
    # Bloch sphere coordinates
    # --------------------------------------------------------

    def bloch_coordinates(self):
        a, b = self.canonical().a, self.canonical().b

        theta = 2 * math.acos(abs(a))
        phi = cmath.phase(b)

        x = math.sin(theta) * math.cos(phi)
        y = math.sin(theta) * math.sin(phi)
        z = math.cos(theta)

        return (x, y, z)

    # --------------------------------------------------------
    # Arithmetic operations
    # --------------------------------------------------------

    def __add__(self, other):
        return Qubit(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Qubit(self.a - other.a, self.b - other.b)

    def __mul__(self, scalar):
        return Qubit(scalar * self.a, scalar * self.b)
    
    def __truediv__(self, scalar):
        return Qubit(self.a / scalar, self.b / scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __neg__(self):
        return Qubit(-self.a, -self.b)

    def __repr__(self):
        return f"Qubit(a={self.a}, b={self.b})"


# ------------------------------------------------------------
# Basis states (must come AFTER class definition)
# ------------------------------------------------------------

ket0 = Qubit(1, 0)
ket1 = Qubit(0, 1)
ket_plus = Qubit(1/math.sqrt(2), 1/math.sqrt(2))
ket_minus = Qubit(1/math.sqrt(2), -1/math.sqrt(2))


# ------------------------------------------------------------
# Standard single-qubit gates
# ------------------------------------------------------------

X = np.array([[0, 1],
              [1, 0]], dtype=complex)

Y = np.array([[0, -1j],
              [1j, 0]], dtype=complex)

Z = np.array([[1, 0],
              [0, -1]], dtype=complex)

H = (1/math.sqrt(2)) * np.array([[1, 1],
                                 [1, -1]], dtype=complex)

S = np.array([[1, 0],
              [0, 1j]], dtype=complex)

T = np.array([[1, 0],
              [0, cmath.exp(1j*math.pi/4)]], dtype=complex)

def R(theta):
    return np.array([
        [math.cos(theta/2), -math.sin(theta/2)],
        [math.sin(theta/2),  math.cos(theta/2)]
    ], dtype=complex)


# ------------------------------------------------------------
# Density matrices
# ------------------------------------------------------------

def density_matrix(qubit):
    a, b = qubit.a, qubit.b
    return np.array([
        [a * a.conjugate(), a * b.conjugate()],
        [b * a.conjugate(), b * b.conjugate()]
    ], dtype=complex)

def mixed_density(states, probs):
    rho = np.zeros((2,2), dtype=complex)
    for q, p in zip(states, probs):
        rho += p * density_matrix(q)
    return rho


# ------------------------------------------------------------
# Tensor product and partial measurement
# ------------------------------------------------------------

def tensor(q1, q2):
    return np.array([
        q1.a * q2.a,
        q1.a * q2.b,
        q1.b * q2.a,
        q1.b * q2.b
    ], dtype=complex)

def measure_first_qubit(state4):
    a00, a01, a10, a11 = state4

    p0 = abs(a00)**2 + abs(a01)**2
    p1 = abs(a10)**2 + abs(a11)**2

    outcome = random.choices([0,1], weights=[p0,p1])[0]

    if outcome == 0:
        collapsed = np.array([a00, a01]) / math.sqrt(p0)
    else:
        collapsed = np.array([a10, a11]) / math.sqrt(p1)

    return outcome, collapsed


# ------------------------------------------------------------
# Expression evaluator
# ------------------------------------------------------------

def evaluate_qubit_expression(expr):
    if "=" in expr:
        _, rhs = expr.split("=", 1)
        expr = rhs.strip()

    expr = expr.replace("sqrt", "math.sqrt")
    expr = expr.replace("pi", "math.pi")
    expr = expr.replace("e^(", "cmath.exp(")
    expr = expr.replace("e^((", "cmath.exp((")
    expr = re.sub(r'(?<!\.)exp\(', 'cmath.exp(', expr)

    allowed = {
        "ket0": ket0,
        "ket1": ket1,
        "ket_plus": ket_plus,
        "ket_minus": ket_minus,
        "math": math,
        "cmath": cmath
    }

    try:
        result = eval(expr, {"__builtins__": {}}, allowed)
    except Exception as e:
        return None, f"Error: {e}"

    if isinstance(result, Qubit):
        return result, f"Valid qubit: {result.is_valid()}"
    else:
        return None, "Expression did not produce a qubit."


# ------------------------------------------------------------
# Interactive console
# ------------------------------------------------------------

def qubit_console():
    print("Enter a qubit expression. Example:")
    print("  1/sqrt(2) * (ket0 - ket1)")
    print("  sqrt(3)/2 * ket0 + 1/3 * ket1")
    print("Type 'quit' to exit.\n")

    while True:
        expr = input(">>> ")
        if expr.lower() == "quit":
            break

        qubit, message = evaluate_qubit_expression(expr)
        print(message)
        if qubit:
            print("Result:", qubit.pretty())
            print("Canonical:", qubit.canonical_pretty())
            print("Norm:", round(qubit.norm(), 6))
            print("P(ket0):", round(qubit.probability_of(ket0), 6))
            print("P(ket1):", round(qubit.probability_of(ket1), 6))
            print("P(ket_plus):", round(qubit.probability_of(ket_plus), 6))
            print("P(ket_minus):", round(qubit.probability_of(ket_minus), 6))
        print()


if __name__ == "__main__":
    qubit_console()
