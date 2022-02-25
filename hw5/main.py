import math


def main(z):
    n = z.__len__()
    counter = 0
    for i in range(1, n+1):
        counter += (math.log(z[n-math.ceil(i/3)], 10) ** 4)
    return counter * 67


if __name__ == "__main__":
    print(main([-0.11, -0.5, -0.55, 0.14, 0.22, 0.64, 0.71, 0.96]))
    print(main([0.87, -0.15, -0.73, -0.97, 0.17, 0.53, 0.55, 0.55]))
