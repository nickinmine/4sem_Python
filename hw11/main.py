import struct


def funcA(p):
    r = dict()
    r['A1'] = struct.unpack('>q', p[4:12])[0]
    r['A2'] = struct.unpack('>d', p[12:20])[0]
    r['A3'] = funcB(p, 20)
    return r
    a2size = struct.unpack('h', p[4:6])[0]
    a2addr = struct.unpack('h', p[6:8])[0]
    t = struct.unpack(str(a2size) + 's', p[a2addr:a2addr + a2size])[0].decode()
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
    r['B1'] = struct.unpack('>b', p[baddr:baddr + 1])[0]
    r['B2'] = struct.unpack('>i', p[baddr + 1:baddr + 5])[0]
    r['B3'] = struct.unpack('>d', p[baddr + 5:baddr + 13])[0]
    a4size = struct.unpack('>Q', p[baddr + 13:baddr + 21])[0]
    a4adrr = struct.unpack('>Q', p[baddr + 21:baddr + 29])[0]
    r['B4'] = list()
    #r['B4'].append(a4size).append(a4adrr)
    r['B5'] = struct.unpack('>b', p[baddr + 29:baddr + 30])[0]
    return r
    gy = struct.unpack('>' + str(a4size) + 'H', p[a4adrr + 36:a4adrr + 36 + a4size])[0]
    return r
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


pack1 = (b"KNTH\x89v\xaf\xdd?o\x0f\x99?\xd4Hn,\x9d\x8c\x88\xc8\xa6:'\xbd?\xecd"
         b'\xb9?\x97\xa3\x04\x00\x00\x00\x02\x00\x00\x00O\xeb\x00\x02\x00S\xe5\x00'
         b'\x00\x00U\x00\x00\x00d\x00\x00\x00s\xee{L"\x00\x00\x00\x02\x00'
         b'\x00\x00\x82\xc6\x1b\xd6#\xd8\xd8\xb0S\xc7\xb2\xd7\xc2tu_\x1a\x82l`1\x86'
         b'\x92%\xc4)x\x15(0\x19\xf8\xb3\x17,\xe14\x1f\x15\x17*M\xa3\x9a\x92_'
         b'#\x95\x1a\xb6\xd6\xe5r3\xe5X2\xb2":\xb0\xbf\x03l\xb7p\xc8jf\xed\xc2HZ\x82'
         b'b\xa4')

pack2 = (b'KNTH\x13$\xad\xcb\x05\xa5 \x1c?\xea\xb8\x15\x1c\x80\xef\xf8\x8d\x91\xa8\xaa'
         b'v?\xd0\xc8\xba\xa3\\\x9a\xb8\x00\x00\x00\x02\x00\x00\x00O/\x00\x03\x00S,\x00'
         b'\x00\x00V\x00\x00\x00e\x00\x00\x00t@\xc6\x8a|\x00\x00\x00\x02\x00'
         b'\x00\x00\x83}\xad\x8d\xfd\xee\xb4\x0fT7[\x94hllr\x85\xa1\x81&\n`'
         b'D\x94\x0b\xe3\xc7j\x01\xfb.\xc7k#\t\xc5\xb6\x0eo\xf3\xdb\x0f_B\\|'
         b'\x02\xef\x85\x8c\xb5\xb6w\xf9s\xd2\x05\xe19\xd7\xa6\xd3q\xd3\x86\xbb\xc6/:J'
         b'\xf9\xbf6Q\r\xf5u')

if __name__ == "__main__":
    print(main(pack1))
    # print(main(pack2))

unpack1 = {'A1': -8541446278474690663,
           'A2': 0.3169207988450542,
           'A3': {'B1': -56,
                  'B2': -1506138179,
                  'B3': 0.8872953645742148,
                  'B4': [51122, 55234],
                  'B5': -21},
           'A4': 'tu',
           'A5': 229,
           'A6': [{'C1': 1595572844, 'C2': 24625, 'C3': 134, 'C4': 10531038986063128624},
                  {'C1': 435729175, 'C2': 11489, 'C3': 52, 'C4': 2239721860145322642},
                  {'C1': 1596167450, 'C2': -18730, 'C3': 229, 'C4': 8229173111106445882}],
           'A7': {'D1': 4001057826,
                  'D2': [12735902036696025194, 7416797777361003172],
                  'D3': -971254237,
                  'D4': -40},
           'A8': [216, 176, 83]}

unpack2 = {'A1': 1379418473366888476,
           'A2': 0.8349710041725293,
           'A3': {'B1': -115,
                  'B2': -1851217290,
                  'B3': 0.2622515292481853,
                  'B4': [14171, 37992],
                  'B5': 47},
           'A4': 'llr',
           'A5': 44,
           'A6': [{'C1': 2241954086, 'C2': 2656, 'C3': 68, 'C4': 10667870587973663534},
                  {'C1': 3345687305, 'C2': -14922, 'C3': 14, 'C4': 8067032216619867260},
                  {'C1': 49251724, 'C2': -19018, 'C3': 119, 'C4': 17974941460461115302}],
           'A7': {'D1': 1086753404,
                  'D2': [15236191590000504634, 5402559468016629109],
                  'D3': 2108526077,
                  'D4': -18},
           'A8': [180, 15, 84]}

if unpack1 == main(pack1):
    print("TRUE")
if unpack2 == main(pack2):
    print("TRUE")
