question = int(input("Which Question: "))

if question == 1:
    def Q1():
        print("Smallest Number: " + str(smallest(15, 10, 25)))
        print("The average value is: " + str(average(15, 10, 25)))

    def smallest(x, y, z):
        if x < y and x < z:
            return (x)
        elif y < x and y < z:
            return (y)
        elif z < x and z < y:
            return (z)
        else:
            return ("Error")

    def average(x, y, z):
        return ((x + y + z)/3)
    print(Q1())
if question == 2:
    def Q2():
        print("All Values Same? " + str(allTheSame(18, 21, 12)))
        print("All Values Different? " + str(allDifferent(18, 21, 12)))
        print("All Values Sorted? " + str(sorted(18, 21, 12)))

    def allTheSame(x, y, z):
        valSame = "FALSE"
        if x == y and x == z:
            valSame = "TRUE"
        return (valSame)

    def allDifferent(x, y, z):
        valDiff = "FALSE"
        if x != y and x != z:
            valDiff = "TRUE"
        return (valDiff)

    def sorted(x, y, z):
        valSorted = "FALSE"
        if x < y and y < z:
            valSorted = "TRUE"
        return (valSorted)
    print(Q2())
if question == 3:
    def Q3():
        print("First digit: " + str(firstDigit(str(6320))))
        print("Last digit: " + str(lastDigit(str(6320))))
        print("Total digits: " + str(digits(str(6320))))
        print("Middle digits: " + str(middledigits(str(6320))))

    def firstDigit(n):
        firstDigit = (n[0])
        return (firstDigit)

    def lastDigit(n):
        lastDigit = (n[3])
        return (lastDigit)

    def digits(n):
        totalDigits = (len(n))
        return (totalDigits)

    def middledigits(n):
        middledigits = (n[1]) + (n[2])
        return (middledigits)
    print(Q3())
