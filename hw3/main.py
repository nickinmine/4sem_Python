import math


def main(n, a, m, b):
    counter = 0
    for c in range(1, n+1):
        counter += 54*c ** 5
    for k in range(1, b+1):
        for j in range(1, m+1):
            for i in range(1, a+1):
                counter += 59*i ** 6 - k ** 5 - math.atan(j)
    return counter


if __name__ == '__main__':
    print(main(6, 6, 7, 2))
    print(main(5, 6, 4, 2))
