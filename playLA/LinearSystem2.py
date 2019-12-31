# python 3.6.4
# encoding: utf-8
from Matrix import Matrix
from Vector import Vector

class LinearSystem:

    """
    m = n 早期版本
    """
    def __init__(self,A,b):
        assert A.row_num() == len(b),\
            "Matrix and Vector Error!"

        self._m = A.row_num()
        self._n = A.col_num()
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                          for i in range(A.row_num())]


    def _max_row(self,index,n):
        best,ret = self.Ab[index][index],index

        for i in range(index+1,n):
            if self.Ab[i][index] > best:
                best = self.Ab[i][index]
                ret = i

        return ret

    def _forward(self):

        n = self._m
        for row_index in range(n):
            max_row = self._max_row(row_index,self._n)
            self.Ab[max_row],self.Ab[row_index] = self.Ab[row_index],self.Ab[max_row]
            # 主元归一化
            if self.Ab[row_index][row_index] == 0:
                # todo
                continue
            self.Ab[row_index] = self.Ab[row_index] / self.Ab[row_index][row_index]

            for j in range(row_index + 1,n):
                self.Ab[j] = self.Ab[j] - self.Ab[row_index] * self.Ab[j][row_index]

    def _backward(self):
        n = self._m
        for row_index in range(n-1,-1,-1):

            for j in range(row_index-1,-1,-1):
                self.Ab[j] = self.Ab[j] - self.Ab[row_index] * self.Ab[j][row_index]

    def guess_jordan_elimination(self):
        self._forward()
        self._backward()

        print(self.Ab)
        pass


if __name__ == '__main__':

    # A = ([[1,2,3],
    #       [4,5,6],
    #       [7,8,9],
    #       [10,11,12]])
    #
    # b = [1,2,3,5]
    #
    #
    #
    # A = Matrix(A)
    # b = Vector(b)
    #
    # # print(LinearSystem(A,b).Ab)
    # print(LinearSystem(A,b)._max_row(3,4))

    # A = [[1,1,1],
    #      [2,1,1],
    #      [1,2,1]]
    # b = [4,5,5]
    #
    # lin_s = LinearSystem(Matrix(A),Vector(b))
    #
    # lin_s.guess_jordan_elimination()

    # A = [[1,1],
    #      [2,1],
    #      [4,2]]
    # b = [3,4,8]

    # A = [[1,1,1,1],
    #      [2,1,1,1],
    #      [1,2,1,1],
    #      [1,2,1,3]]
    # b = [10,11,12,20]

    A = [[1,1,1,1],
         [2,4,2,2,],
         [1,3,2,1],
         [1,2,3,1]]

    b = [10,24,17,18]
    LinearSystem(Matrix(A),Vector(b)).guess_jordan_elimination()