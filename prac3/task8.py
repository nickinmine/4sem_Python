from matplotlib import pyplot, colors
from numpy import random


def sprite():
    s = random.randint(0, 2, 25).reshape(5,5)
    for i in range(3):
        for j in range(5):
            s[j][i] = s[j][4-i]
    return s


def printSprite(sprite):
    for i in range(5):
        for j in range(5):
            print(sprite[i][j], end=' ')
        print()


if __name__ == "__main__":
    s = sprite()
    printSprite(s)
    f, a = pyplot.subplots()
    a.imshow(s, cmap=colors.ListedColormap(['white', 'black']))
    pyplot.show()
