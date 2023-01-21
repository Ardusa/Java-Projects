import math
q = int(input("Which Question: "))

if q == 1:
    number = input("Enter a number: ")
    number = eval(number)

    print("All squares less than ", number, ":")
    k = 0
    while (k ** 2 < number):
        print(k ** 2, end = ' ')
        k = k + 1

    k = 0
    print("\n\nAll positive numbers that are divisible by 10 and less than ", number, ":")
    while (k * 10 < number):
        if k * 10 > 0:
            print(k * 10, end = ' ')
        k = k + 1

    k = 0
    print("\n\nAll powers of 2, less than ", number, ":")
    while (2 ** k < number):
        print(2 ** k, end = ' ')
        k = k + 1

if q == 2:
    k = 0
    for x in range(2, 101):
        if x % 2 == 0:
            k += x
    print("Sum of all even numbers from 2 to 100: ", k)
    k = 0
    for x in range(1, 101):
        k += x ** 2
    print("\n\nSum of all squares 1 to 100: ", k)

if q == 3:
    for i in range(1, 10, 2):
        print(i)