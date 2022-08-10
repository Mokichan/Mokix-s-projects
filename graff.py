from matplotlib import pyplot as plt


def s_plit(str):
    return str.split()


def graf(a, b, c, n):
    if a == 0:
        raise Exception("А не должно быть нулевым")
    x = [i for i in range(-n, n + 1)]
    y = [(a * i ** 2) + (b * i) + c for i in range(-n, n + 1)]
    plt.plot(x, y)
    plt.show()