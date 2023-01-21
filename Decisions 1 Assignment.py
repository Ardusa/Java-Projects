assignment = input("Which HW question are you on: ")
assignment = eval(assignment)
if assignment == 1:
    number = input("Please enter number: ")
    number = eval(number)
    OGnumber = number

    # Negative Numbers
    if number < 0:
        number = number*-1

    # 1
    if number >= 0:
        digits = 1

    # 10
    if number >= 10:
        digits = 2

    # 100
    if number >= 100:
        digits = 3

    # 1,000
    if number >= 1000:
        digits = 4

    # 10,000
    if number >= 10000:
        digits = 5

    # 100,000
    if number >= 100000:
        digits = 6

    # 1,000,000
    if number >= 1000000:
        digits = 7

    # 10,000,000
    if number >= 10000000:
        digits = 8

    # 100,000,000
    if number >= 100000000:
        digits = 9

    # 1,000,000,000
    if number >= 1000000000:
        digits = 10

    print(OGnumber, " has ", digits, " digits.")

if assignment == 2:
    string = "all different"

    number1 = input("Enter First Number: ")
    number2 = input("Enter Second Number: ")
    number3 = input("Enter Third Number: ")

    number1 = eval(number1)
    number2 = eval(number2)
    number3 = eval(number3)

    if number1 == number2:
        if number1 == number3:
            string = "All the same"
    print(string)

if assignment == 3:
    string = "not in order"

    number1 = input("Enter First Number: ")
    number2 = input("Enter Second Number: ")
    number3 = input("Enter Third Number: ")

    number1 = eval(number1)
    number2 = eval(number2)
    number3 = eval(number3)

    if number1 < number2:
        if number2 < number3:
            string = "in order"
    print(string)
