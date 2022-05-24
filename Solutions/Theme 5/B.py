from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, listing):
        self.listing = deepcopy(listing)
        self.rows = len(listing)
        self.columns = len(listing[0])

    def __str__(self):
        res = ''
        for line in self.listing:
            res += '\t'.join(map(str, line))+'\n'
        return res[:-1]

    def size(self):
        return self.rows, self.columns

    def __add__(self, mat2):
        newmat = deepcopy(self)
        for i in range(self.rows):
            for j in range(self.columns):
                newmat.listing[i][j] += mat2.listing[i][j]
        return newmat

    def __mul__(self, alpha):
        newmat = deepcopy(self)
        for i in range(newmat.rows):
            for j in range(newmat.columns):
                newmat.listing[i][j] *= alpha
        return newmat

    __rmul__ = __mul__


exec(stdin.read())
