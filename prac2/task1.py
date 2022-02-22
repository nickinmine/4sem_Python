import math

def init1(x):
    return x ** 42

def init2(x):
    if x < 0.5:
        return x * x
    return math.sqrt(x-0.5)

def init3(x):
    return ((x ** 3 + x ** 8 / 26) / (x ** 7 - math.cos(x))) ** 0.5 + (math.log(x, math.e) + x ** 3 + 29) ** 0.5 + (
                67 * x ** 4 - math.sin(x))

def init4():
    counter = 0
    for i in range(0, 11):
        counter += (complex(0, 17)) ** 5 - (complex(0, 1)) ** 7 + 24
        return 75 * counter

def init5(x):
    res = 0
    for i in range(11):
        res += x ** 5 - x
    return 42 * res

def init6(x):
    counter = 1
    for i in range(1, 11):
        counter *= x * math.sqrt(i)
    return counter

def init7(x, n):
    counter = 0
    for i in range(0, n + 1):
        for j in range(1, n + 1):
            counter += (x ** i) + (x ** (2 * j))
    return counter * 0.5

def init8(n):
    if n == 0:
        return 3
    return math.sin(init8(n - 1)) - (1 / 16) * init8(n - 1) ** 3

def init9(x):
    counter = 0
    for i in x:
        counter += x[i] ** 2
    return math.sqrt(counter)
