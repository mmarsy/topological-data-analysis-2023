import random
import time
import numpy as np

from field import FSFElement
from matrix import FieldMatrix


def get_key(d, val):
    for key, value in d.items():
        if val == value:
            return key

    return "key doesn't exist"


def matrix_dic_to_table(d):
    result = []
    for key in d:
        temp_order = list(d[key].keys())
        temp_order.sort()
        temp = [d[key][i] for i in temp_order]
        result.append(temp)
    return result


def rank(matrix, char=None):
    matrix1 = FieldMatrix(matrix, char)
    return matrix1.rank()


def ker(matrix):
    dim_of_domain = len(matrix)
    return dim_of_domain - rank(matrix)


def no_square(n):
    result = set()
    for i in range(1, n + 1):
        good = True
        for k in range(2, i + 1):
            if i % (k ** 2) == 0:
                good = False
        if good:
            result.add(i)
    return result


class SimplicialComplex(list):
    def __init__(self, n):
        super().__init__()
        # self.vertices = set(range(1, n+1))
        self.vertices = no_square(n)
        self.append([])
        self.enumerations = []

        def check_if_finished():
            for i in self.vertices:
                for lst in self:
                    if lst:
                        if i % lst[-1] == 0 and i > lst[-1]:
                            if lst + [i] not in self:
                                self.append(lst + [i])
                                return False
            return True

        while True:
            extended = random.choice(self)
            for number in self.vertices:
                if not extended:
                    if [number] not in self:
                        self.append([number])
                else:
                    if number % extended[-1] == 0 and number > extended[-1]:
                        if extended + [number] not in self:
                            self.append(extended + [number])
            if check_if_finished():
                self.remove([])
                break
        self.underlying_spaces = {n - 1: {index: val for index, val in enumerate([lst for lst in self if len(lst) == n])}
                                  for n in self.vertices}
        self.underlying_spaces[-1] = {0: []}

    def del_matrix(self, n):
        result = {}
        domain = self.underlying_spaces[n]
        image = self.underlying_spaces[n - 1]
        if n == 0:
            return {face: {0: 0} for face in domain}

        for face in domain:
            temp = {}
            for i in range(len(domain[face])):
                temp_face = domain[face][:i] + domain[face][i + 1:]
                temp[get_key(image, temp_face)] = (-1) ** (i + 1)
            for key in image:
                temp[key] = temp.get(key, 0)
            result[face] = temp
        return result

    def homology_group(self, n):
        k = matrix_dic_to_table(self.del_matrix(n))
        i = matrix_dic_to_table(self.del_matrix(n + 1))
        print(f'dim ker del_{n} = {ker(k)}, dim im del_{n + 1} = {rank(i)}')
        return ker(k) - rank(i)

    def euler_characteristic(self):
        result = 0
        for dim in self.underlying_spaces:
            if dim >= 0:
                result += ((-1) ** dim) * len(self.underlying_spaces[dim])
        return result


def main():
    n = 100
    t = time.time()
    a = SimplicialComplex(n)
    # print(time.time() - t)
    # print(a)
    for key in a.underlying_spaces:
        if len(a.underlying_spaces[key]) > 0:
            print(f'{key}: ({len(a.underlying_spaces[key])}), {a.underlying_spaces[key]}')
    print(a.euler_characteristic())


def test():
    print(no_square(10))


if __name__ == '__main__':
    main()
