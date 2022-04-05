class Test1:
    a = 0
    val = 0

    def __init__(self):
        self.a = 2
        self.val = 3.14
        pass

    def init(self, a, val):
        self.a = a
        self.val = val
        pass

    def toString(self):
        return "a = " + str(self.a) + " , val = " + str(self.val)

class Test2:
    def func(self):
        return "Ok"


if __name__ == "__main__":
    obj = Test1()
    obj.init(4.3, 259259)
    obj2 = Test1()
    print(obj.toString())
    print(obj2.toString())
    obj1 = Test2()
    k = input()
    if k == "func":
        print(obj1.func())
