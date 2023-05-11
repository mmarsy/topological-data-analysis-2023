import random
import time
import numpy as np


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


def rank(matrix):
    matrix1 = np.array(matrix)
    return np.linalg.matrix_rank(matrix1)


def ker(matrix):
    dim_of_domain = len(matrix)
    return dim_of_domain - rank(matrix)


class SimplicialComplex(list):
    def __init__(self, n):
        super().__init__()
        self.vertices = set(range(1, n+1))
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


class SimplicialComplex2(list):
    def __init__(self, n):
        super().__init__()
        self.vertices = set(range(1, n+1))
        self.append([])

        def check_if_finished():
            for lst in self:
                for i in self.vertices:
                    if lst:
                        if i % lst[-1] == 0 and i > lst[-1]:
                            if lst + [i] not in self:
                                self.append(lst + [i])
                                return check_if_finished()
                    else:
                        if [i] not in self:
                            self.append([i])
                            return check_if_finished()

        check_if_finished()
        self.remove([])
    

def main():
    n = 50
    t = time.time()
    a = SimplicialComplex(n)
    # print(time.time() - t)
    # print(a)
    for key in a.underlying_spaces:
        print(f'{key}: {a.underlying_spaces[key]}')

    for i in range(n-1):
        try:
            print(a.homology_group(i))
        except KeyError:
            pass


if __name__ == '__main__':
    main()
