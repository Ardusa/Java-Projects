import math

problem = input("Which HW question are you on: ")
problem = eval(problem)

if problem == 1:
    card = input("Enter the card notation (ALL CAPS): ")
    suit = "Error"
    card_number = "Error"

    if card[1] == "D":
        suit = "Diamonds"
    elif card[1] == "H":
        suit = "Hearts"
    elif card[1] == "S":
        suit = "Spades"
    elif card[1] == "C":
        suit = "Clubs"
    else:
        print("Type the number or letter of the card, followed by the suit of the card. Ex. QS for Queen of Spades.")

    if card[0] == "1":
        card_number = "1"
    elif card[0] == "2":
        card_number = "2"
    elif card[0] == "3":
        card_number = "3"
    elif card[0] == "4":
        card_number = "4"
    elif card[0] == "5":
        card_number = "5"
    elif card[0] == "6":
        card_number = "6"
    elif card[0] == "7":
        card_number = "7"
    elif card[0] == "8":
        card_number = "8"
    elif card[0] == "9":
        card_number = "9"
    elif card[0] == "10":
        card_number = "10"
    elif card[0] == "J":
        card_number = "Jack"
    elif card[0] == "Q":
        card_number = "Queen"
    elif card[0] == "K":
        card_number = "King"
    else:
        print("Type the number or letter of the card, followed by the suit of the card. Ex. QS for Queen of Spades.")

    print(card_number + " of " + suit)
elif problem == 2:
    unit1 = input("Unit Converting from (all lowercase): ")
    unit2 = input("Unit Converting to (all lowercase): ")

    rate = 1
    unit_1 = ""
    unit_2 = ""

    if unit1 == "fl oz":
        unit_1 = "Fluid Ounces"
        if unit2 == "ml":
            rate = 29.5735
            unit_2 = "Milliliters"
        elif unit2 == "l":
            rate = 0.0296
        else:
            print("Error")

    elif unit1 == "gal":
        unit_1 = "Gallons"
        if unit2 == "ml":
            rate = 3785.4118
            unit_2 = "Milliliters"
        elif unit2 == "l":
            rate = 3.7854
            unit_2 = "Liters"
        else:
            print("Error")

    elif unit1 == "oz":
        unit_1 = "Ounces"
        if unit2 == "g":
            rate = 28.35
            unit_2 = "Grams"
        elif unit2 == "kg":
            rate = 0.0283
            unit_2 = "Kilograms"
        else:
            print("Error")

    elif unit1 == "lb":
        unit_1 = "Pounds"
        if unit2 == "g":
            rate = 453.592
            unit_2 = "Grams"
        elif unit2 == "kg":
            rate = 0.454
            unit_2 = "Kilograms"
        else:
            print("Error")

    elif unit1 == "in":
        unit_1 = "Inches"
        if unit2 == "mm":
            rate = 25.4
            unit_2 = "Millimeters"
        elif unit2 == "cm":
            rate = 0.394
            unit_2 = "Centimeters"
        elif unit2 == "m":
            rate = 0.0254
            unit_2 = "Meters"
        else:
            print("Error")

    elif unit1 == "ft":
        unit_1 = "Feet"
        if unit2 == "mm":
            rate = 304.8
            unit_2 = "Millimeters"
        elif unit2 == "cm":
            rate = 30.48
            unit_2 = "Centimeters"
        elif unit2 == "m":
            rate = 3.05
            unit_2 = "Meters"
        elif unit2 == "km":
            rate = 0.000305
            unit_2 = "Kilometers"
        else:
            print("Error")

    elif unit1 == "mi":
        unit_1 = "Miles"
        if unit2 == "mm":
            rate = 1609344
            unit_2 = "Millimeters"
        elif unit2 == "cm":
            rate = 160934.4
            unit_2 = "Centimeters"
        elif unit2 == "m":
            rate = 1609.344
            unit_2 = "Meters"
        elif unit2 == "km":
            rate = 1.609
            unit_2 = "Kilometers"
        else:
            print("Error")

    else:
        print("Error")

    x = input("Quantity of " + unit_1 + " :")
    x = eval(x)
    y = x * rate

    print(x, unit_1, " = ", y, unit_2)
elif problem == 3:
    number = input("Enter positive integer: ")
    #number = eval(number)

    numberVal = eval(number)

    if len(number) > 0:
        ones = number[len(number)-1]
        ones = eval(ones)
    if len(number) > 1:
        tens = number[len(number)-2]
        tens = eval(tens)
    if len(number) > 2:
        hundreds = number[len(number)-3]
        hundreds = eval(hundreds)
    if len(number) > 3:
        thousands = number[len(number)-4]
        thousands = eval(thousands)

    random = 0
    romanVal = ""
    romanNumerals = ""
    romanOnes = ""
    romanTens = ""
    romanHundreds = ""
    romanThousands = ""

    if numberVal == 0:
        print("Number must be greater than 0.")
    elif numberVal >= 4000:
        print("Number must be lower than 4,000.")
    elif numberVal == 10:
        romanVal = 'X'
    elif numberVal == 100:
        romanVal = 'C'
    elif numberVal == 1000:
        romanVal == 'M'
    else:
        random = 1

    # Ones Place
    if random == 0:
        print("")
    elif ones < 4:
        romanOnes = ('I' * ones)
    elif ones < 6:
        romanOnes = ('I' * (5 - ones)) + 'V'
    elif ones < 9:
        romanOnes = 'V' + ('I' * (ones - 5))
    else:
        romanOnes = ((10 - ones) * 'I') + 'X'
    # Tens Place
    if numberVal < 10:
        print("")
    elif random == 0:
        print("")
    elif tens < 4:
        romanTens = 'X' * tens
    elif tens < 6:
        romanTens = ('X' * (5 - tens)) + 'L'
    elif tens < 9:
        romanTens = 'L' + ('X' * (tens - 5))
    else:
        romanTens = ((10 - tens) * 'X') + 'C'
    # Hundreds Place
    if numberVal < 100:
        print("")
    elif random == 0:
        print("")
    elif hundreds < 4:
        romanHundreds = 'C' * hundreds
    elif hundreds < 6:
        romanHundreds = ('C' * (5 - hundreds)) + 'D'
    elif hundreds < 9:
        romanHundreds = 'C' + ('C' * (hundreds - 5))
    else:
        romanHundreds = ((10 - hundreds) * 'C') + 'M'
    # Thousands Place
    if numberVal < 1000:
        print("")
    elif random == 0:
        print("")
    elif thousands < 4:
        romanThousands = 'M' * thousands
    else:
        print("Invalid Entry. Number must be between 1 & 3,999")

    print("Ones ", romanOnes)
    print("Tens ", romanTens)
    print("Hundreds ", romanHundreds)
    print("Thousands ", romanThousands)

    romanNumerals = "" + romanThousands + romanHundreds + romanTens + romanOnes + ""

    print("Roman Numeral Conversion: ", romanNumerals)

    print("Invalid Question")
