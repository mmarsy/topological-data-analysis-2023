import math
import pandas as pd


def circle_gen(r=1, n=6):
    for i in range(n):
        yield Point(math.sin(math.pi * i / n), math.cos(math.pi * i / n)) * r


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, other):
        return Point(other * self.x, other * self.y)

    def __repr__(self):
        return repr([self.x, self.y])


class Circle:
    def __init__(self, r=1, n=6):
        x_c = [i.x for i in circle_gen(r, n)]
        y_c = [i.y for i in circle_gen(r, n)]

        self.d = pd.DataFrame({'x': x_c, 'y': y_c})

    def __repr__(self):
        return self.d.__repr__()

    def __getitem__(self, item):
        return self.d[item]


def main():
    circles = [Circle(r=1, n=n) for n in range(3, 10)]
    results = [circ['x'].var() for circ in circles]
    print(results)


if __name__ == '__main__':
    main()
