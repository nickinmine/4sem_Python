

def main(x, y):
    r = x;
    for i in range(0, y - 1):
        x = x + r
    return x;

def test():
    for i in range(0, 100):
        for j in range(0, 100):
            assert main(i, j) == i*j, 'errorka'

if __name__ == '__main__':
    test()
