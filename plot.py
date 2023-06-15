import matplotlib.pyplot as plt
from main import SimplicialComplex


def main(n):
    domain = list(range(5, n))
    image = [SimplicialComplex(i).euler_characteristic() for i in domain]
    plt.plot(domain, image)
    plt.show()


if __name__ == '__main__':
    n = 500
    main(n)
