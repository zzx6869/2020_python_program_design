import math


def fac(y):
    if y + 1 < 0:
        return "None"
    x = math.sqrt(y + 1)
    return x


z = fac(float(input()))
print(z)
