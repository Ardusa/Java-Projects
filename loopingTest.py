x = 0

for x in range(1,11):
    string = ""
    y = 0
    for y in range(1,11):
        string = string + (str(x*y) + "\t")
    print(string)
