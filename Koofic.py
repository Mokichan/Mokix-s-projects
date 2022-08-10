from math import sqrt


def s_plit(str):
    return str.split()


def korny(a, b, c):
    if a == 0:
        raise Exception("А не должно быть нулевым")
    D = (b ** 2) - (4 * a * c)
    if D > 0:
        x1 = (- b + sqrt(D)) / (2 * a)
        x2 = (- b - sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = - b / (2 * a)
        return x
    else:
        return "Нет корней"