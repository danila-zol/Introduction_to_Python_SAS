# This class defines a vector with a few simple operations over it

class Vector:
    def __init__(self, l):
        if type(l) != list:
            print("Cannot initialize Vector from " + str(type(l)))
            return

        for e in l:
            if type(e) != float and type(e) != int:
                print("Vector can only have float or int values, not " + str(type(e)))
                return

        self._vec = l

    def get_elements(self):
        return self._vec

    def set_element(self, pos: int, val: float):
        if type(val) != float:
            print("Vector can only have float or int values, not " + str(type(val)))
            return

        self._vec[pos] = val
    

    def __add__(self, n):
        r = []
        for e in self._vec:
            r.append(e + n)

        return r

    def __mul__(self, n):
        r = []
        for e in self._vec:
            r.append(e * n)

        return r

    @staticmethod
    def zeroes(n):
        return [0 for i in range(n)]

v1 = Vector([1, 2, 3])
print(v1.get_elements())
print(v1 + 10)
zeroes = Vector.zeroes(4)
print(zeroes)