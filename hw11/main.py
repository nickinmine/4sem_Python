import struct


def funcA(p):
    r = dict()
    r['A1'] = struct.unpack('>q', p[4:12])[0]
    r['A2'] = struct.unpack('>d', p[12:20])[0]
    r['A3'] = funcB(p, 20)
    a2size = struct.unpack('h', p[4:6])[0]
    a2addr = struct.unpack('h', p[6:8])[0]
    t = struct.unpack(str(a2size)+'s', p[a2addr:a2addr+a2size])[0].decode()
    r['A2'] = t
    baddr = struct.unpack('h', p[8:10])[0]
    r['A3'] = funcB(p, baddr)
    r['A4'] = struct.unpack('i', p[10:14])[0]
    a5size = struct.unpack('h', p[14:16])[0]
    a5addr = struct.unpack('I', p[16:20])[0]
    r['A5'] = list(struct.unpack(str(a5size) + 'b', p[a5addr:a5addr + a5size]))
    r['A6'] = funcE(p[20:])
    return r


def funcB(p, baddr):
    r = dict()
    r['B1'] = struct.unpack('>h', p[baddr:baddr + 2])[0]
    r['B2'] = struct.unpack('>q', p[baddr + 4:baddr + 12])[0]
    r['B2'] = struct.unpack('>d', p[baddr + 12:baddr + 20])[0]
    a4size = struct.unpack('>Q', p[baddr + 20:baddr + 28])[0]
    a4adrr = struct.unpack('>Q', p[baddr + 28:baddr + 36])[0]
    gy = struct.unpack('>' + str(a4size) + 'H', p[a4adrr + 36:a4adrr + 36 + a4size])[0]
    caddrlist = struct.unpack('4I', p[baddr + 12:baddr + 28])
    r['B3'] = list()
    for caddr in caddrlist:
        r['B3'].append(funcC(p, caddr))
    r['B4'] = funcD(p, baddr + 28)
    return r


def funcC(p, caddr):
    r = dict()
    r['C1'] = list(struct.unpack('6b', p[caddr:caddr + 6]))
    r['C2'] = struct.unpack('i', p[caddr + 6:caddr + 10])[0]
    return r


def funcD(p, daddr):
    r = dict()
    r['D1'] = struct.unpack('f', p[daddr:daddr + 4])[0]
    d2size = struct.unpack('H', p[daddr + 4:daddr + 6])[0]
    d2addr = struct.unpack('H', p[daddr + 6:daddr + 8])[0]
    r['D2'] = list(struct.unpack(str(d2size) + 'b', p[d2addr:d2addr + d2size]))
    return r


def funcE(p):
    r = dict()
    r['E1'] = struct.unpack('B', p[:1])[0]
    r['E2'] = struct.unpack('B', p[1:2])[0]
    r['E3'] = struct.unpack('Q', p[2:10])[0]
    r['E4'] = struct.unpack('Q', p[10:18])[0]
    return r


def main(pack):
    return funcA(pack)


pack = (b"KNTH\x89v\xaf\xdd?o\x0f\x99?\xd4Hn,\x9d\x8c\x88\xc8\xa6:'\xbd?\xecd"
 b'\xb9?\x97\xa3\x04\x00\x00\x00\x02\x00\x00\x00O\xeb\x00\x02\x00S\xe5\x00'
 b'\x00\x00U\x00\x00\x00d\x00\x00\x00s\xee{L"\x00\x00\x00\x02\x00'
 b'\x00\x00\x82\xc6\x1b\xd6#\xd8\xd8\xb0S\xc7\xb2\xd7\xc2tu_\x1a\x82l`1\x86'
 b'\x92%\xc4)x\x15(0\x19\xf8\xb3\x17,\xe14\x1f\x15\x17*M\xa3\x9a\x92_'
 b'#\x95\x1a\xb6\xd6\xe5r3\xe5X2\xb2":\xb0\xbf\x03l\xb7p\xc8jf\xed\xc2HZ\x82'
 b'b\xa4')

if __name__ == "__main__":
    print(main(pack))

unpack = {'A1': 226,
          'A2': 'wzdl',
          'A3': {'B1': 3294186994,
                 'B2': 2403630181684677044,
                 'B3': [{'C1': [-64, -2, 9, 73, 51, -76], 'C2': 1549067098},
                        {'C1': [-3, 86, 67, -10, 119, 34], 'C2': 1794550907},
                        {'C1': [94, -122, 115, 95, 11, -79], 'C2': -1099199769},
                        {'C1': [-65, 10, 84, 17, 120, -24], 'C2': -1955813496}],
                 'B4': {'D1': 0.23836566507816315, 'D2': [46, 74]}},
          'A4': -189752400,
          'A5': [-8, -76],
          'A6': {'E1': 251,
                 'E2': 26,
                 'E3': 10863273395041409237,
                 'E4': 1614939997103482178}}

if unpack == main(pack):
    print("TRUE")
