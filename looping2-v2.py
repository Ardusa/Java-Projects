question = input("Which Question are you on: ")
question = eval(question)

if (question == 1):
    # Q1
    integers = input("How many integers: ")
    integers = eval(integers)
    integers = integers + 1

    #
    max = 0
    min = 100
    evenNums = 0
    oddNums = 0
    value = 0

    for k in range(1, integers):
        exec(f'num{k} = 0')

    for k in range(1, integers):
        value = input("Enter a number: ")
        f'num{k} = {int} + r"(" {value} + r")"'
        value = int(value)

        if (value > max):
            max = value
        if (value < min):
            min = value

        if (value % 2 == 0):
            evenNums = evenNums + 1
        else:
            oddNums = oddNums + 1

    print("Largest Input:", max)
    print("Smallest Input:", min)
    print("\n\nNumber of Even inputs:", evenNums)
    print("Number of Odd Inputs:", oddNums)

if (question == 2):
    number = int(input("Enter a value: "))
    digits = 0
    digit1 = 0
    digit2 = 0
    digit3 = 0
    digit4 = 0

    if (number - 10 <= 0):
        digits = 1
    elif (number - 100 <= 0):
        digits = 2
    elif (number - 1000 <= 0):
        digits = 3
    else:
        digits = 4

    number = str(number)

    if (digits >= 4):
        digit1 = int(number[0])
    if (digits >= 3):
        digit2 = int(number[1])
    if (digits >= 2):
        digit3 = int(number[2])
    if (digits >= 1):
        digit4 = int(number[3])
    else:
        print("Invalid Input")

    print(digit1, digit1 + digit2, digit1 + digit2 +
          digit3, digit1 + digit2 + digit3 + digit4)

if (question == 3):
    string = input("\nEnter String: ")

    output = "Uppercase Letters: "
    for ch in string:
        if ch >= "A" and ch <= "Z":
            output = output + str(ch) + " "

    print(output)

    output = "Second Letter of every word: "
    for k in range(len(string)):
        if k % 2 == 0:
            output = output + string[k] + " "

    output = 'All vowels replaced with "_": '
    string2 = string
    string2 = string2.replace("a", "_")
    string2 = string2.replace("e", "_")
    string2 = string2.replace("i", "_")
    string2 = string2.replace("o", "_")
    string2 = string2.replace("u", "_")

    print(output + string2)

    output = "# of digits in string: "
    x = len(string)

    print(output + str(x))

    output = "The positions of all vowels in string: "

    for k in range(0, len(string), 1):
        if string[k] == "a" or string[k] == "e" or string[k] == "i" or string[k] == "o" or string[k] == "u":
            if k+1 >= len(string):
                print(output + str(k + 1))
#                print(k + 1, end='\n')
            else:
                print(k + 1, end='. ')
