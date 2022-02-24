import math


def main(n):
    counter = 0
    if n == 0:
        return 0.03
    if n >= 1:
        counter += 56*math.log(18+main(n-1) ** 2+main(n-1)) ** 2
    return counter


if __name__ == "__main__":
    print(main(5))
    print(main(3))
