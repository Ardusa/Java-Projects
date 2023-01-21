listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def question(q, functions):
    qLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    qString = [
        "Swap the first and last elements in the list:",
        "Shift all elements by one to the right and move the last element into the first position:",
        "Replace all even elements with 0:",
        "Remove the middle element if the list length is odd, or the middle two elements if the length is even:",
        "Return the largest and smallest element in the list:",
        "Return True if the list is currently sorted in increasing order:",
        "Return True if the list contains duplicate elements:"
    ]
    print(qLetters[q] + '. ' + qString[q] + '\n\t', end=" ")
    print(functions[q])


def A(data):
    if len(data) == 0:
        return

    temp = data[0]
    data[0] = data[len(data) - 1]
    data[len(data) - 1] = temp
    return data


def B(data):
    if len(data) == 0:
        return

    temp = data[-1]
    for i in range(-1, -1 * len(data), -1):
        data[i] = data[i-1]
    data[0] = temp
    return data


def C(data):
    if len(data) == 0:
        return

    temp = 0
    for i in range(len(data)):
        if data[i] % 2 == 0:
            data[i] = temp
    return data


def D(data):
    if len(data) == 0:
        return

    if len(data) % 2 == 0:
        middle = int((len(data) / 2) - 1)
        del data[middle]
    if len(data) % 2 != 0:
        middle = int((len(data) - 1) / 2)
        del data[middle]
    return data


def E(data):
    if len(data) == 0:
        return

    max = data[0]
    min = data[0]
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
        if data[i] < min:
            min = data[i]
    return ('Largest Element: ' + str(max) + '\tSmallest Element: ' + str(min))


def F(data):
    if len(data) == 0:
        return

    temp = 0
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            temp = temp + 1
    if temp == (len(data) - 1):
        return 'True'
    else:
        return 'False'


def G(data):
    if len(data) == 0:
        return

    value = 0
    for x in range(len(data)):
        for y in range(len(data)):
            if data[x] == data[y]:
                value = value + 1
    if value == len(data):
        return 'False'
    else:
        return 'True'


functions = [A(data=list(listNum)), B(data=list(listNum)), C(data=list(listNum)), D(
    data=list(listNum)), E(data=list(listNum)), F(data=list(listNum)), G(data=list(listNum))]

print('\nThe original data for all functions is: ', listNum)
for i in range(7):
    print(" ")
    question(i, functions)
