#def printTriangle(sideLength):
#    if sideLength < 1: return
#    printTriangle(sideLength-1)
#    print("[]" * sideLength)
#sideLength = int(input("Please enter a number: "))
#printTriangle(sideLength)

deduct = 1
x = 0
n = 0

def output(number):
    
    if (number - deduct) <= x:
        print(n)
    else:
        #number = number - deduct    #149,139,39,
        number = number - deduct
        x = x - deduct              #-1,-11,-111,
        deduct = deduct * 10        #10,100,1000,
        n = n + 1
        output(number)
        
number = int(input("Enter Integer: "))
output(number)
