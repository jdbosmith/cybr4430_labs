#  function that takes a well formed complex number in cartesian form as its input and returns the polar representation of its input.
import math


def toPolar(c1):
    #Complete the function
    import cmath
    import math

    r = abs(c1)
    theta = math.degrees(cmath.phase(c1))
    return r, int(theta)

    
#  function that takes a well formed polar representation of a complex number as its input and returns the cartesian representation of its input.
def toCart(mag, angle):
    #Complete the function
    import cmath
    import math

    radians = math.radians(angle)
    x = mag * math.cos(radians)
    y = mag * math.sin(radians)
    return x + y*1j

    
# function that takes two complex numbers in polar form as its inputs and returns the product of its two inputs in polar form.
def multPolar(m1, a1, m2, a2):
    #Complete the function
    import cmath
    import math

    # Multiply magnitudes
    magnitude = m1 * m2
    
    # Add angles
    angle = a1 + a2
    
    return (magnitude, angle)
