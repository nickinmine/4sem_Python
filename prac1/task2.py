
def main():
    a = 99999
    b = 1000000000
    c = a**a + b
    print(c)

def erg():
    a = 0.954992586021436
    b = a**a
    print(b)

def value42():
    print(42)
    if 42.0 == 42:
        print(1)
    print(42.0)
    print(42e0)
    print()
    print("42")
    print('42')
    print("4"+"2")
    print('4'+'2')
    print(-(-42))
    print(int('101010', base=2))
    print(int('22', base=20))
    print(4_2)

if __name__ == '__main__':
    value42()
