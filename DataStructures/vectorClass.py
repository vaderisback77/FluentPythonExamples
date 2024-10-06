# Defining the two dimensional vector class with attributes x, y
import math


class Vector:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'


    def __add__(self, other):
        """Adds vectors

        v1 = Vector(2, 2)
        v2 = Vector(4, 4)
        v3 = v1 + v2 = Vector(6, 6)

        Args: 
            other (instance object): Second vector argument

        Returns:
            _type_: Vector instance
        """
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)

    def __mul__(self, value):
        """Multiplication

        v1 = Vector(2, 2)
        v1 * 3
        = Vector(6, 6)

        Args:
            value (int): integer value

        Returns:
            _type_: Vector instance
        """
        # x = value * self.x
        # y = value * self.y
        return Vector(self.x * value, self.y * value)

    def __abs__(self):
        """Calculates absolute value for an instance Object

        Returns:
            _type_: float value
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """Calculates boolean value for an instance object

        Returns:
            _type_: bool value
        """
        return bool(abs(self))


v1 = Vector(2, 2)
v2 = Vector(3, 3)

# additon
v3 = v1 + v2
print(v3)

# multiplication
v3 = v1 * 2
print(v3)

# absolute value
v3 = abs(v1)
print(v3)

# boolean value
v3 = bool(v1)
print(v3)

'''
Output:
Vector(5, 5)
Vector(4, 4)
2.8284271247461903
True
'''