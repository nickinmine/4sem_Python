class Main(object):
    def __init__(self):
        self.a = "A"

    def melt(self):
        if self.a == "A":
            self.a = "B"
            return 0
        if self.a == "B":
            self.a = "F"
            return 3
        else:
            raise KeyError()

    def clear(self):
        if self.a == "B":
            self.a = "B"
            return 4
        if self.a == "C":
            self.a = "D"
            return 5
        if self.a == "E":
            self.a = "F"
            return 8
        else:
            raise KeyError()

    def close(self):
        if self.a == "A":
            self.a = "C"
            return 1
        if self.a == "B":
            self.a = "C"
            return 2
        if self.a == "C":
            self.a = "C"
            return 6
        if self.a == "D":
            self.a = "E"
            return 7
        else:
            raise KeyError()


if __name__ == "__main__":
    o = Main()
    print(o.melt())  # 0
    print(o.clear())  # 4
    print(o.clear())  # 4
    print(o.close())  # 2
    print(o.close())  # 6
    print(o.clear())  # 5
    print(o.close())  # 7
    print(o.clear())  # 8
