import math


def main(z):
    counter = 65*(z ** 3) + 34*(math.acos(79*z ** 3) ** 2)
    counter -= (28*(7*z ** 2) ** 6 + 91*(1-(z ** 3)/74) ** 5)
    return counter


if __name__ == '__main__':
    print(main(-0.14))
