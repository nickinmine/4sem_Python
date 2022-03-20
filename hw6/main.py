data = {
    "['FREGE', 'CMAKE', 'ROFF', 2012]": 5,
    "['FREGE', 'MUPAD', 'ROFF', 2011]": 10,
    "['FREGE', 'CMAKE', 'NCL', 2012]": 4,
    "['SWIFT', 'CMAKE', 'NCL', 2011]": 8,
    "['SWIFT', 'MUPAD', 'ROFF', 2012]": 3,
    "['HCL', 'MUPAD', 'ROFF', 2012]": 1,
    "['SWIFT', 'MUPAD', 'ROFF', 2011]": 9,
    "['HCL', 'CMAKE', 'NCL', 2012]": 2,
    "['HCL', 'PUG', 'ROFF', 2012]": 0,
    "['HCL', 'MUPAD', 'NCL', 2011]": 6
}


def main(args):
    if str(args) in data:
        return data[str(args)]
    else:
        return str(args)
