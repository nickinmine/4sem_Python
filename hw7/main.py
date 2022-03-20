def bitset(value, begin, end):
    mask = 0
    for i in range(begin, end):
        mask |= 1 << i
    return value & mask


def main(value):
    temp = bitset(value, 29, 32) >> 21
    temp |= bitset(value, 27, 29) << 3
    temp |= bitset(value, 23, 27) >> 20
    temp |= bitset(value, 20, 23) >> 20
    temp |= bitset(value, 14, 20) >> 3
    temp |= bitset(value, 1, 14) << 16
    temp |= bitset(value, 0, 1) << 7
    return temp


if __name__ == "__main__":
    print(main(0xed39323c))
    print(main(0x58fae9f7))
