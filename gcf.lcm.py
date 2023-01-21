import math

def bigNum(x,y):
    bigNum = 0
    if x > y:
        bigNum = x
    elif y > x:
        bigNum = y
    else:
        bigNum = x    
    return bigNum

def gcf(x,y):
    value = 0
    dividend = bigNum(x,y)

    while((dividend > 1) and (value != 1)):
        if (x % dividend) == 0 and (y % dividend) == 0:
            value = 1
        else:
            dividend = dividend - 1
    
    return dividend

def lcm(x,y):
    value = 0
    multiple = bigNum(x,y)

    while(value != 1):
        if (multiple % x) == 0 and (multiple % y) == 0:
            value = 1
        else:
            multiple = multiple + 1
    
    return multiple

x = int(input('#1: '))
y = int(input('#2: '))

print('\nGreatest Common Factor:', gcf(x,y))
print('Least Common Multiple:', lcm(x,y))