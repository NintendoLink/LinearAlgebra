# python 3.6.4
# encoding: utf-8
from Matrix import Matrix
from Vector import Vector
from _global import is_zero,is_equal

class LinearSystem:

    def __init__(self,A,b):
        assert A.row_num() == len(b),\
            "Matrix and Vector Error!"

        self._m = A.row_num()
        self._n = A.col_num()
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                          for i in range(A.row_num())]

        # 记录主元的位置信息
        self.pivots = []


    def _max_row(self,index_i,index_j,n):

        best,ret = self.Ab[index_i][index_j],index_i

        for i in range(index_i+1,n):
            if abs(self.Ab[i][index_j]) > best:
                best = self.Ab[i][index_j]
                ret = i

        return ret

    def _forward(self):

        i,k = 0,0 #i,k为主元
        while i < self._m and k < self._n:
            max_row = self._max_row(i,k,self._m)
            self.Ab[max_row],self.Ab[i] = self.Ab[i],self.Ab[max_row]
            if is_zero(self.Ab[i][k]):
                k += 1
            else:
            # 主元归一化
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i+1,self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]
                self.pivots.append(k)
                k += 1
                i += 1

    def _backward(self):
        n = len(self.pivots)
        for i in range(n-1,-1,-1):

            k = self.pivots[i]
            # A[i][k] 为主元
            for j in range(i-1,-1,-1):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)),end=" ")
            print("|",self.Ab[i][-1])

    def guess_jordan_elimination(self):
        self._forward()
        self._backward()

        # print(self.Ab)
        # pass


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

    # A = [[1,1,1,1],
    #      [2,4,2,2,],
    #      [1,3,2,1],
    #      [1,2,3,1]]
    #
    # b = [10,24,17,18]

    # A = [[0,0,2,3,2],
    #      [1,3,2,1,5],
    #      [2,2,4,4,3],
    #      [1,1,4,3,5]]
    # b = [28,42,49,52]

    A = [[1,2,3],
         [3,2,1],
         [4,5,6]]

    b = [16,8,34]
    # LinearSystem(Matrix(A),Vector(b)).guess_jordan_elimination()
    lin_sys = LinearSystem(Matrix(A),Vector(b))
    lin_sys.guess_jordan_elimination()
    lin_sys.fancy_print()

