# no. 2
inputstr = input("Enter a string: ")
print("\nUppercase Letters:", end=' ')
for ch in inputstr:
    if ch >= "A" and ch <= "Z":
        print(ch, end=' ')
print("\nSecond letter in string: ", end='')
for i in range(len(inputstr)):
    if i % 2 == 0:
        print(inputstr[i], end=',')
print("\nUnderscore replacement: ", end='')
inputstr1 = inputstr.replace("a", "_")
inputstr1 = inputstr1.replace("e", "_")
inputstr1 = inputstr1.replace("i", "_")
inputstr1 = inputstr1.replace("o", "_")
inputstr1 = inputstr1.replace("u", "_")
print(inputstr1)
print("Number of digits: ", end='')
sum = 0
for i in inputstr:
    if i != " ":
        sum += 1
print(sum, "digits")
print("Index of vowels:", end=' ')
for i in range(0, len(inputstr), 1):
    if inputstr[i] == "a" or inputstr[i] == "e" or inputstr[i] == "i" or inputstr[i] == "o" or inputstr[i] == "u":
        if i+1 >= len(inputstr):
            print(i+1, end='\n')
        else:
            print(i+1, end=', ')
