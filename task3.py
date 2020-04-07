""" Module for vector operations """
EPSILON = 0.001

#version3
class Vector:
    """ Class representing vector """
    def __init__(self, vector: [tuple, list]):
        self.check_input(vector)
        self.vector = vector

    def check_input(self, vector: [tuple, list]) -> None:
        """Check input.

        Args:
            self(:obj:`Vector`): input argument during class initialization.

        Raises:
            TypeError: If input isinstance is not tuple or list
            TypeError: If input tuple/list contains some elements
            that are not float/int
            - raise isinstanceError.
        """
        if not isinstance(vector, tuple) and not isinstance(vector, list):
            raise TypeError("expected Any[Tuple[Any[float, int]],"
                            + "List[Tuple[Any[float, int]]].")

        for elem in vector:
            if not isinstance(elem, float) and not isinstance(elem, int):
                raise TypeError("expected Any[Tuple[Any[float, int]],"
                                + "List[Tuple[Any[float, int]]].")

    def length(self) -> float:
        """Length of vector

        Length of vector is a square root of the sum of the squared elements

        """
        return sum([elem ** 2 for elem in self.vector]) ** 0.5

    def __lt__(self, other) -> bool:
        """ Overload "<" operator and check vectors' shapes

        Args:
            self(:obj:`Vector`): left-side Vector
            other(:obj:`Vector`): right-side Vector

        Raises:
            ValueError: If vectors' shape mismatch
        """
        if len(self.vector) != len(other.vector):
            raise ValueError("vectors shape mismatch.")
        return self.length() < other.length()

    def __eq__(self, other) -> bool:
        """ Overload "=" operator and check vectors' shapes

        If absolute difference between lengths of vectors < EPSILON
        vectors are consider equal, otherwise they are different.

        Args:
            self(:obj:`Vector`): left-side Vector
            other(:obj:`Vector`): right-side Vector

        Raises:
            ValueError: If vectors' shape mismatch
        """
        if len(self.vector) != len(other.vector):
            raise ValueError("vectors shape mismatch.")
        return abs(self.length() - other.length()) <= EPSILON

    def __le__(self, other) -> bool:
        """ Overload "<=" operator

        For this overload we can use before used overloads
        for "<" and "==" operators.

        Args:
            self(:obj:`Vector`): left-side Vector
            other(:obj:`Vector`): right-side Vector
        """
        return self < other or self == other
