import cmath
import math

class Qubit:
    def __init__(self, a, b):
        self.a = complex(a)
        self.b = complex(b)

    def norm(self):
        return abs(self.a)**2 + abs(self.b)**2

    def is_valid(self, tol=1e-12):
        return abs(self.norm() - 1) < tol

    def __add__(self, other):
        return Qubit(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Qubit(self.a - other.a, self.b - other.b)

    def __mul__(self, scalar):
        return Qubit(scalar * self.a, scalar * self.b)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __repr__(self):
        return f"Qubit(a={self.a}, b={self.b})"


# Basis states
ket0 = Qubit(1, 0)
ket1 = Qubit(0, 1)
ket_plus = Qubit(1/math.sqrt(2), 1/math.sqrt(2))
ket_minus = Qubit(1/math.sqrt(2), -1/math.sqrt(2))


def evaluate_qubit_expression(expr):
    # Strip assignment if present
    if "=" in expr:
        _, rhs = expr.split("=", 1)
        expr = rhs.strip()

    # Replace sqrt with math.sqrt
    expr = expr.replace("sqrt", "math.sqrt")
    
    # Allow e^(...) syntax
    expr = expr.replace("e^(", "cmath.exp(")

    # Allow exp(...) syntax safely
    expr = expr.replace("exp(", "cmath.exp(")

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
            print("Result:", qubit)
        print()


if __name__ == "__main__":
    qubit_console()
