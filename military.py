import math

timeOne = int(input("Start Time: "))
#timeOne = eval(timeOne)
timeTwo = int(input("End Time: "))
#timeTwo = eval(timeTwo)

if (timeTwo > timeOne):
    minutes = (timeTwo - timeOne)%100
    hours = (timeTwo - timeOne)//100

else:
    minutes = (timeOne - timeTwo)%100
    hours = ((2400 - timeOne) + timeTwo)//100

print(hours, " hours and ", minutes, "minutes")
