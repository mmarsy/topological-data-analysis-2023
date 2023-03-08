import pandas as pd
import matplotlib.pyplot as plt
import math as m


def sphere_gen(r=1, n=6):
    for i in range(n):
        for j in range(n):
            yield {'x': r * m.cos(2 * m.pi * i / n),
                   'y': r * m.sin(2 * m.pi * i / n) * m.cos(2 * m.pi * j / n),
                   'z': r * m.sin(2 * m.pi * i / n) * m.sin(2 * m.pi * j / n)}


def main():
    for d in sphere_gen():
        print(d['x'] ** 2 + d['y'] ** 2 + d['z'] ** 2)

    x = [d['x'] for d in sphere_gen()]
    y = [d['y'] for d in sphere_gen()]
    z = [d['z'] for d in sphere_gen()]

#    ax = plt.figure().add_subplot(projection='3d')
#    ax.scatter(x, y, z)
#    plt.show()

    df = pd.DataFrame([d for d in sphere_gen(1, 10)])
    print(df)


if __name__ == '__main__':
    main()