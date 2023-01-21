question = int(input("Question #? "))
if question == 1:
    deduct = 1
    x = 0
    n = 0

    def output(num, deduct, x, n):
        if num - deduct < x:
            print(n)
        else:
            n = n + 1
            num = num - deduct  # 149,
            x = x - deduct  # -1,
            deduct = deduct * 10  # 10
            output(num, deduct, x, n)

    number = int(input("Please Enter Integer: "))
    output(number, deduct, x, n)

if question == 2:
    def calc(x, y, max):
        if x > max:
            print(str(max) + '! =', y)
        else:
            y = x * y
            calc(x+1, y, max)

    variable = 1
    total = 1

    multiple = int(input("Enter a number to calculate its factorial: "))
    calc(variable, total, multiple)

if question == 3:
    def reverseStr(string):
        if len(string) == 0:
            return (string)
        else:
            return reverseStr(string[1:]) + string[0]

    def isPalindrome(string):
        if string == reverseStr(string):
            print(string + " is a Palindrome!")
        else:
            print(string + " is not a Palindrome")

    string = input("Enter a word to check if it is a palindrome: ")
    isPalindrome(string)
