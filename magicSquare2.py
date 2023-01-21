# Python3 program to check whether a given
# matrix is magic matrix or not
# Returns true if mat[][] is magic
# square, else returns false.
def isMagicSquare(mat):
    n = len(mat)
    # sumd1 and sumd2 are the sum of the two diagonals
    sumd1 = 0
    sumd2 = 0
    for i in range(n):
        # (i, i) is the diagonal from top-left -> bottom-right
        # (i, n - i - 1) is the diagonal from top-right -> bottom-left
        sumd1 += mat[i][i]
        sumd2 += mat[i][n-i-1]
        # if the two diagonal sums are unequal then it is not a magic square
    if not (sumd1 == sumd2):
        return False
    for i in range(n):
        #sumr is rowsum and sumc is colsum
        sumr = 0
        sumc = 0
        for j in range(n):
            sumr += mat[i][j]
            sumc += mat[j][i]
        if not (sumr == sumc == sumd1):
            return False
        # if all the conditions are satisfied then it is a magic square
    return True


if (isMagicSquare()):
    print("Magic Square")
else:
    print("Not a magic Square")


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
