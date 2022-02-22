
def init():
    return (True * 2 + False) * -True

def init2():
    return (1 < 42 == 42)

def init3():
    return (0.3 + 0.6)-0.9 == 0 #== 0.9

if __name__ == '__main__':
    print(init())
    print(init2())
    print(init3())
    #init4(x/0;)


