from functools import reduce


def euklides(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def euklidesMod(a, b):
    if a <= b:
        return euklidesMod(b, a)
    elif b == 0:
        return a
    else:
        return euklidesMod(b, a % b)


def euklides_multi(*args):
    return reduce(euklides, args)
