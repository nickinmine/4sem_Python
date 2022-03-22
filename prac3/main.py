import random
import sys
import obj

def print(arg):
    arg = str(arg)
    return sys.stdout.write(arg)


def println(arg):
    arg = str(arg)
    return sys.stdout.write(arg + "\n")


if __name__ == "__main__":
    print(2)
    print("erbhreh")
    println('')
    println(obj.init())
    println(obj.init())
