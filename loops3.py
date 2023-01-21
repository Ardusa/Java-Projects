import random

question = int(input("What question: "))

if question == 1:
    num = [0,0,0,0,0,0,0,0,0,0]
    quantity = [0,0,0,0,0,0,0,0,0,0]

    for k in range(10):
        num[k] = 0

        quantity[k] = 0

    ranNum = 0

    for i in range(50):
        ranNum = random.randint(1,10)

        num[ranNum-1] = num[ranNum-1] + ranNum

    k = 0

    for k in range(10):
        quantity[k] = num[k] / (k + 1)

        print(str(k+1) + ":", quantity[k])

if question == 2:
    y = random.randint(1,3)

    if y == 1:
        pick = "Rock"
    elif y == 2:
        pick = "Paper"
    else:
        pick = "Scissors"

    x = int(input("Rock, Paper, Scissors (1, 2, 3): "))

    print("Your opponent picked: " + pick)
    print("")

    if y == x:
        print("You tied!")
    elif y == 1:
        if x == 2:
            print("You Won!")
        else:
            print("You Lost!")
    elif y == 2:
        if x == 1:
            print("You Lost!")
        else:
            print("You Won!")
    elif y == 3:
        if x == 1:
            print("You Win!")
        else:
            print("You Lost!")
    else:
        print("invalid input")

if question == 3:
    value = int(input("Enter integer: "))
    div = 2

    while(value/div >= 2):
        if value%div < 1:
            print(div)
            value = value/div
        else:
            div = div + 1
    print(int(value))

if question == 4:
    string = input("Enter your word: ")
    strLen = len(string)

    for k in range(strLen):
        print(string[k])

    k = 0

    for k in range(strLen - 1):
        print(string[k] + string[k+1])
    
    k = 0

    for k in range(strLen - 2):
        print(string[k] + string[k+1] + string[k+2])

