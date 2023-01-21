question = int(input("Question #? "))

if question == 1:
    def caseFind(string, y):
        caseUp = 0
        caseDown = 0
        k = 0
        x = len(string)
        string2 = string.upper()

        for k in range(0, x):
            ch1 = string[k]
            ch2 = string2[k]
            if (ch1 != ' ' and ch2 != ' '):
                if (ch1 == ch2):
                    caseUp = caseUp + 1
                else:
                    caseDown = caseDown + 1
        if y == 1:
            return (caseUp)
        elif y == 2:
            return (caseDown)
        else:
            return ()
        

    strInput = input("Enter a string: ")
    print("\nNo. of Uppercase letters:", caseFind(strInput, 1))
    print("No. of Lowercase letters:", caseFind(strInput, 2))

if question == 2:
    def calc(x, y, z):
        if z == 1:
            return (x+y)
        elif z == 2:
            return (x-y)
        elif z == 3:
            return (x*y)
        elif z == 4:
            return (x/y)
        else:
            return ("Incorrect Operation")
