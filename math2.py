import math

l1 = input("Length (1) = ")
l2 = input("Length (2) = ")
l3 = input("Length (3) = ")

l1 = eval(l1)
l2 = eval(l2)
l3 = eval(l3)

perimeter = (l1+l2+l3)
area = (math.sqrt(perimeter/2(perimeter/2-l1)(perimeter/2-l2)(perimeter/2-l3)))

print("Perimeter = ", perimeter)
print("Area = ", area)
