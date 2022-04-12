import struct


def funcA(p):
    r = dict()
    r['A1'] = struct.unpack('>q', p[4:12])[0]
    r['A2'] = struct.unpack('>d', p[12:20])[0]
    r['A3'] = funcB(p, 20)
    c2size = struct.unpack('>H', p[42:44])[0]
    c2addr = struct.unpack('>H', p[44:46])[0]
    r['A4'] = (struct.unpack('>' + str(c2size) + 'c',
                             p[c2addr:c2addr + c2size])[0] +
               struct.unpack('>' + str(c2size) + 'c',
                             p[c2addr:c2addr + c2size])[1]).decode()
    r['A5'] = struct.unpack('>B', p[46:47])[0]
    caddr = struct.unpack('>I', p[47:51])[0]
    t1 = funcC(p, caddr)
    caddr = struct.unpack('>I', p[51:55])[0]
    t2 = funcC(p, caddr)
    caddr = struct.unpack('>I', p[55:59])[0]
    t3 = funcC(p, caddr)
    r['A6'] = [t1, t2, t3]
    r['A7'] = funcD(p, 59)
    r['A8'] = list(struct.unpack('>' + str(3) + 'B', p[76:79]))
    return r


def funcB(p, index):
    r = dict()
    r['B1'] = struct.unpack('>b', p[index:index + 1])[0]
    r['B2'] = struct.unpack('>i', p[index + 1:index + 5])[0]
    r['B3'] = struct.unpack('>d', p[index + 5:index + 13])[0]
    a4size = struct.unpack('>L', p[index + 13:index + 17])[0]
    a4adrr = struct.unpack('>L', p[index + 17:index + 21])[0]
    r['B4'] = list(struct.unpack('>' + str(a4size) + 'H',
                                 p[a4adrr:a4adrr + a4size * 2]))
    r['B5'] = struct.unpack('>b', p[index + 21:index + 22])[0]
    return r


def funcC(p, index):
    r = dict()
    r['C1'] = struct.unpack('>I', p[index:index + 4])[0]
    r['C2'] = struct.unpack('>h', p[index + 4:index + 6])[0]
    r['C3'] = struct.unpack('>B', p[index + 6:index + 7])[0]
    r['C4'] = struct.unpack('>Q', p[index + 7:index + 15])[0]
    return r


def funcD(p, index):
    r = dict()
    r['D1'] = struct.unpack('>L', p[index:index + 4])[0]
    size = struct.unpack('>L', p[index + 4:index + 8])[0]
    adrr = struct.unpack('>L', p[index + 8:index + 12])[0]
    r['D2'] = list(struct.unpack('>' + str(size) + 'Q',
                                 p[adrr:adrr + size * 8]))
    r['D3'] = struct.unpack('>i', p[index + 12:index + 16])[0]
    r['D4'] = struct.unpack('>b', p[index + 16:index + 17])[0]
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
    #print(main(pack1))
    print(main(pack2))


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
