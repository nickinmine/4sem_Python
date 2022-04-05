def main(oldlst):
    lst = []
    [lst.append(x) for x in oldlst if x not in lst]
    for i in range(len(lst)):
        lst[i].pop(4)
        lst[i].pop(2)
        lst[i].pop(1)
    for i in lst:
        i[0] = i[0].replace(".", "-")
        i[1] = i[1].replace("@", "[at]")
        i[2] = i[2][9:]
    lst = transpose(lst)
    return lst


def transpose(lst):
    res = []
    for j in range(len(lst[0])):
        t = []
        for i in range(len(lst)):
            t += [lst[i][j]]
        res += [t]
    return res


test1 = [["21.02.02", "", "kelizuk50@rambler.ru",  "kelizuk50@rambler.ru",     "", "+7 (507) 294-02-23"],
         ["17.04.99", "", "gavotidi38@rambler.ru", "gavotidi38@rambler.ru",    "", "+7 (460) 610-06-84"],
         ["28.04.01", "", "rizberg64@gmail.com",   "rizberg64@gmail.com",      "", "+7 (887) 254-36-97"],
         ["17.04.99", "", "gavotidi38@rambler.ru", "gavotidi38@rambler.ru",    "", "+7 (460) 610-06-84"]]

if __name__ == "__main__":
    print(test1)
    print(main(test1))
