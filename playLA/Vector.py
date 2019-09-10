# python 3.6.4
# encoding: utf-8

class Vector:

    """
    Zero Vector
    """
    @classmethod
    def zero(cls,dim):
        return cls([0] * dim)

    def __init__(self,lst):
        self._values = lst

    """
    Call by system
    """
    def __repr__(self):
        return "Vector({})".format(self._values)

    "Call by users"
    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))

    """
    Get vactor's length
    """
    def __len__(self):
        return len(self._values)

    """
    Get element from vector by index(weidu)
    """
    def __getitem__(self, index):
        return self._values[index]

    """
    Return iteractor 
    """
    def __iter__(self):
        return self._values.__iter__()
    """
    Add operator
    """
    def __add__(self, other):
        assert len(self) == len(other),\
        "Error in adding,length of vectors must be same"

        return Vector([a+b for a,b in zip(self._values,other)])
    """
    Sub operator
    """
    def __sub__(self, other):
        assert len(self) == len(other),\
        "Error in sub,length of vectors must be same"
        return Vector([a-b] for a,b in zip(self._values,other))
    """
    Multi operator
    """
    def __mul__(self, k):
        return Vector([k * v for v in self._values])

    """
    Reverse Multi operator
    """
    def __rmul__(self, k):
        return self * k

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self
if __name__ == '__main__':
    vector = Vector([1,2,3,4,5])
    print(vector)

    # for i in vector:
    #     print(i)

    vector2 = Vector([2,4,6,8,10])

    print("{} + {} = {}".format(vector,vector2,vector+vector2))

    vactor3 = Vector.zero(5)

    print(vactor3)

    print("{} + {} = {}".format(vector,vactor3,vactor3+ vector))