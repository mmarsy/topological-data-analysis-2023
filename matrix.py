from field import FSFElement


def inverse(x):
    if isinstance(x, FSFElement):
        return x.inverse()
    return 1 / x


def sub_lists(a, b):
    return [x - y for x, y in zip(a, b)]


def mul_list(a, scalar):
    return [x * scalar for x in a]


def is_zero(x):
    if isinstance(x, FSFElement):
        return x.is_zero()
    return x == 0


def is_zero_list(lst):
    return all([is_zero(x) for x in lst])


class Matrix(list):
    def __init__(self, lst):
        super().__init__()
        for col in lst:
            self.append(col)
        self.to_eliminate = lst

    def gauss_elimination(self, to_print=False):
        step = 0
        appendix = 0
        working_matrix = self.to_eliminate
        dim = min(len(working_matrix), len(working_matrix[0]))
        ready = False

        while not ready:
            for i in range(step, len(working_matrix)):
                if not is_zero(working_matrix[step][step + appendix]):
                    ready = True
                    break
                working_matrix = working_matrix[:step] + working_matrix[step + 1:] + [working_matrix[step]]
            if not is_zero(working_matrix[step][step + appendix]):
                ready = True
            else:
                appendix += 1

        while step < dim:
            # we want rank, so this operation does not matter
            working_matrix[step] = mul_list(working_matrix[step], inverse(working_matrix[step][step + appendix]))
            pivot = working_matrix[step]

            if to_print:
                print(f'step={step}, wm={working_matrix}')
            for i in range(step + 1, len(working_matrix)):
                # if not is_zero(pivot[step]):
                if to_print:
                    print(f'59: i={i}, {working_matrix}')
                working_matrix[i] = sub_lists(working_matrix[i],
                                              mul_list(pivot, working_matrix[i][step + appendix] / pivot[step + appendix]))

            step += 1
            for i in range(step, dim):
                if not is_zero(working_matrix[step][step + appendix]):
                    break
                working_matrix = working_matrix[:step] + working_matrix[step + 1:] + [working_matrix[step]]
            if step < dim:
                while is_zero(working_matrix[step][step + appendix]):
                    step += 1
                    if step >= dim:
                        break

        self.to_eliminate = working_matrix
        return appendix

    def rank(self):
        self.gauss_elimination()
        return len([lst for lst in self.to_eliminate if not is_zero_list(lst)])


class FieldMatrix(Matrix):
    def __init__(self, lst, char=None):
        if char is None:
            def _init(x):
                return x
        else:
            def _init(x):
                return FSFElement(x, char)
        for col in lst:
            self.append([_init(x) for x in col])

        self.to_eliminate = [[_init(x) for x in col] for col in lst]


m = FieldMatrix([[0, 1, -1, 2, 2],
                [0, 2, -2, 1, 0],
                [0, -1, 2, 1, -2],
                [0, 2, -1, 122, 0]], 7)
m.gauss_elimination()
m.gauss_elimination()
print(m.to_eliminate)
print(m.rank())
