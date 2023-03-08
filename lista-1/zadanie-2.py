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

#    ax = plt.figure().add_subplot(projection='3d')
#    ax.scatter(x, y, z)
#    plt.show()

    df = pd.DataFrame([d for d in sphere_gen(1, 4)])
    df.append(pd.DataFrame([d for d in sphere_gen(3, 4)]))
    print(df)

    df_t = pd.DataFrame([{1: 1}])
    df_t.append([{1: 2}])
    print(df_t)


if __name__ == '__main__':
    main()
