def fast_mul():
    a = int(input())
    b = int(input())
    counter = 0
    if a % 2 != 0:
        counter += b
    while True:
        if a <= 1:
            break
        a, b = a // 2, b * 2
        if a % 2 != 0:
            counter += b
    return counter

def fast_pow():
    a = int(input())
    b = int(input())
    counter = 1
    while b:
        if b % 2 != 0:
            counter *= a
        b //= 2
        a *= a
    return counter

if __name__ == '__main__':
    print(fast_mul())
    print(fast_pow())