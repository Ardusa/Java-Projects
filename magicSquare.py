def printTable(table):
    for i in range(4):
        for j in range(4):
            print("%8d" % table[i][j], end="")
        print()


def makeTable(string):
    table = [
        [string[0], string[1], string[2], string[3]],
        [string[4], string[5], string[6], string[7]],
        [string[8], string[9], string[10], string[11]],
        [string[12], string[13], string[14], string[15]]
    ]
    printTable(table)


def stringCreation(string):
    val = 0
    i = 0
    num = [0] * 16
    for k in range(16):
        number = string[i] + string[i+1]
        val = int(number)
        num[k] = val
        i = i+3
    return num


string = input("Enter string: ")
makeTable(stringCreation(string))

#   01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16
