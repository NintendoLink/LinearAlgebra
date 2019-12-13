# python 3.6.4
# encoding: utf-8
import math
from _global import EPSILON
class Vector:

    @classmethod
    def zero(cls,dim):
        return cls([0] * dim)
    def __init__(self,lst):
        self._values = lst

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __iter__(self):
        return self._values.__iter__()

    def __add__(self, another):
        assert len(self) == len(another),\
            "Error in adding.Length of vectors must be same"
        return Vector([a+b for a,b in zip(self,another)])

    def __sub__(self, another):
        assert len(self) == len(another), \
            "Error in subing.Length of vectors must be same"
        return Vector([a-b for a,b in zip(self,another)])

    def __mul__(self, k):
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        return (1 / k) * self
    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self) )

    def normalize(self):
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error,vector norm is zero!")
        return (1 / self.norm()) * self

if __name__ == '__main__':

    # u = Vector([1,2,3])
    # print(u)
    # print(len(u))

    # vec1 = Vector([1,2,3])
    # vec2 = Vector([2,3,4])
    #
    # print("{} + {} = {}".format(vec1,vec2,vec1 + vec2))
    # print("{} - {} = {}".format(vec1,vec2,vec1 - vec2))
    # print("{} * {} = {}".format(vec1,2,vec1 * 2))
    # print("{} * {} = {}".format(vec1,2,2 * vec1))
    #
    # zero = Vector.zero(5)
    # print(zero)

    # vec = Vector([3,4])
    # print("Vector:".format(vec))
    # print(vec.norm())
    # print(vec.normalize())
    zero_vec = Vector.zero(2)
    print(zero_vec.normalize())