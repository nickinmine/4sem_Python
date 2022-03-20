def main(input):
    while '  ' in input:
        input = input.replace('  ', ' ')
    input = input[input.find('.do')+3:input.find('.end')]
    input = input.replace('>><<', '\0').replace('>> <<', '\0')
    input = input.replace('>>', '').replace('<<', '').strip()

    rawSplit1 = input.split('\0')
    for i in range(len(rawSplit1)):
        rawSplit1[i] = rawSplit1[i].strip()
    rawSplit2 = []
    for s in rawSplit1:
        rawSplit2.append(s.split('::='))
        rawSplit2[len(rawSplit2) -
                  1][0] = rawSplit2[len(rawSplit2)-1][0][3:].strip()
        rawSplit2[len(rawSplit2) -
                  1][1] = rawSplit2[len(rawSplit2)-1][1][7:].replace(' ', '')
        rawSplit2[len(rawSplit2) -
                  1][1] = rawSplit2[len(rawSplit2)-1][1].replace(')', '')
        rawSplit2[len(rawSplit2) -
                  1][1] = rawSplit2[len(rawSplit2)-1][1].replace('#', '')
        rawSplit2[len(rawSplit2) -
                  1][1] = rawSplit2[len(rawSplit2)-1][1].split('.')
        for i in range(len(rawSplit2[len(rawSplit2) -
                                     1][1])):
            rawSplit2[len(rawSplit2) -
                      1][1][i] = int(rawSplit2[len(rawSplit2) -
                                               1][1][i])
    result = {}
    for s in rawSplit2:
        result[s[0]] = s[1]
    return result


print(main('.do << let cedi_433::= array( #3455 .#3895 .#-9958 . #6714 ) >>        <<let usteis ::=array( #-7917 . #3935 . #-3181) >>.end'))