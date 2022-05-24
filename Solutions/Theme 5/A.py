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


exec(stdin.read())
