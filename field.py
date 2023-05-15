def eea(a, b, x=1, y=0):
    # Base Case
    if a == 0:
        return 0, 1

    x1, y1 = eea(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return x, y


class FSFElement:
    @staticmethod
    def check_chars(a, b):
        if a.char != b.char:
            raise ValueError('INCOMPATIBLE CHARACTERS')

    def __init__(self, val, char=2):
        self.val = val
        self.char = char

    def is_zero(self):
        return self.val % self.char == 0

    def __eq__(self, other):
        if self.char != other.char:
            return False
        if (self.val - other.val) % self.char == 0:
            return True
        return False

    def __add__(self, other):
        FSFElement.check_chars(self, other)
        return FSFElement(self.val + other.val, self.char)

    def __mul__(self, other):
        try:
            return FSFElement(self.val * other.val, self.char)
        except AttributeError:
            return FSFElement(self.val * other, self.char)

    def __sub__(self, other):
        return self + other * -1

    def __repr__(self):
        return str(self.val % self.char)

    def inverse(self):
        if self.val % self.char == 0:
            raise ZeroDivisionError

        if self.val % self.char == 1:
            return FSFElement(1, self.char)

        if self.val % self.char == self.char - 1:
            return FSFElement(-1, self.char)

        x, y = eea(self.val, self.char)
        return FSFElement(x, self.char)

    def __truediv__(self, other):
        return self * other.inverse()


def test():
    a = FSFElement(4, 7)
    b = FSFElement(9, 2)
    print(a.inverse())


if __name__ == '__main__':
    test()
