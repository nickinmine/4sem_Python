import math


def main(x):
    counter = 0
    if x < 157:
        counter = (abs(x) ** 5)+(math.log(x, 2) ** 3)+x
    if 157 <= x < 257:
        counter = 1 + abs(60*x) ** 2
    if 257 <= x < 289:
        counter = x ** 7
    if 289 <= x < 310:
        counter = 41*(math.sin(x) ** 4) - (x ** 7)/53
    if x >= 310:
        counter = 79*(x ** 6) + 29*x + math.cos(x) ** 4
    return counter


if __name__ == '__main__':
    print(main(310))
