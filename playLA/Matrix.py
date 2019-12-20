# python 3.6.4
# encoding: utf-8
from Vector import Vector
class Matrix:

    @classmethod
    def zero(cls,row,col):

        return Matrix([[0] * col] * row)

    def __init__(self,list2d):
        self._values = [row[:] for row in list2d]
    def __repr__(self):
        return "Matrix:{}".format(self._values)
    __str__ = __repr__

    def row_num(self):
        return len(self._values)
    __len__ = row_num

    def col_num(self):
        return len(self._values[0])

    def shape(self):
        return (self.row_num(),self.col_num())

    def size(self):
        return self.row_num() * self.col_num()

    def __getitem__(self, pos):
        row,col = pos
        return self._values[row][col]

    def row_vector(self,index):
        return Vector(self._values[index])

    def col_vector(self, index):
        return Vector([lst[index] for lst in self._values])

    def __add__(self, another):
        assert self.shape() == another.shape(), \
            "Error in Matrix Adding,The Matrix shape must be same"
        return Matrix([[a + b for a,b in zip(self.row_vector(i),another.row_vector(i))] for i in range(self.row_num())])

    def __sub__(self, another):
        assert self.shape() == another.shape(),\
            "Error in Matrix Subbing,The Matrix shape must be same"
        return Matrix([[a - b for a,b in zip(self.row_vector(i),another.row_vector(i))] for i in range(self.row_num())])

    def __mul__(self, k):
        return Matrix([[a * k for a in self.row_vector(i)] for  i in range(self.row_num())])

    def __rmul__(self, k):
        return self.__mul__(k)

    def __truediv__(self, k):
        assert  k != 0,\
        "Error in Divving"
        return self * (1 / k)

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def dot(self,another):
        if isinstance(another,Vector):
            assert len(another) == self.col_num(),\
                "Matrix dot Vector Error"
            return Vector([self.row_vector(index).dot(another) for index in range(self.row_num())])

        elif isinstance(another,Matrix):
            assert self.col_num() == another.row_num(),\
                "Matrix dot error,row col can't be correspend"

            # return Matrix([[self.row_vector(row_index).dot(another.col_vector(col_index))
            #                     for row_index in range(self.row_num())]
            #                         for col_index in range(another.col_num())])
            return Matrix([[self.row_vector(row_index).dot(another.col_vector(col_index))
                                for col_index in range(another.col_num())]
                                    for row_index in range(self.row_num())])
            pass
        else:
            print("Error in Matrix dot.")
if __name__ == '__main__':
    mat1 = Matrix([[1,2,3],[4,5,6]])
    # print(mat1)
    # print(mat1.row_num())
    # print(mat1.col_num())
    # print(mat1.shape())
    # print(mat1.size())
    #
    # print(mat1[1,2])
    #
    # print(mat1.row_vector(1))
    # print(mat1.col_vector(2))

    mat2 = Matrix([[2,4,6],[8,10,15]])

    print(mat1 + mat2)

    print(mat2 - mat1)

    print(mat1 * 2)
    print(mat1 / 2)

    print(Matrix.zero(2,3))

    vec = Vector([1,2,3])
    print(mat1.dot(vec))

    mat3 = Matrix([[4,3],
                   [2,1],
                   [6,5]])

    print(mat1.dot(mat3))