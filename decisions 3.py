problem = input("Which HW question are you on: ")
problem = eval(problem)

if problem == 1:
    cost = int(input("Please Enter Cost Of Groceries: "))

    #total = eval(cost)
    coupon = 0

    if cost < 10:
        coupon = 0
    elif 10 < cost < 60:
        coupon = ((cost)*.08)
    elif 60 < cost < 150:
        coupon = ((cost)*.10)
    elif 150 < cost < 210:
        coupon = ((cost)*.12)
    else:
        coupon = ((cost)*.14)

    val = coupon/cost

    print("You win a discount coupon of $",
          coupon, "(", val, "% of your purchase )")
if problem == 2:
    bill = input("Bill Amount: ")
    happy = input(
        "On a scale of 1-3, how satisfied were you with our service today?")
    happy = eval(happy)
    bill = eval(bill)

    if happy == 1:
        tip = 20
    elif happy == 2:
        tip = 15
    elif happy == 3:
        tip = 10
    else:
        print("Satisfaction level not valid.")

    billTotal = bill*(1 + (tip/100))
    tipAmount = bill*(tip/100)

    print("_________________________________")
    print("Bill\t\t\t$", bill)
    print("Satisfaction Rating\t", happy)
    print("Tip %\t\t\t", tip, "%")
    print("Tip Amount\t\t$", tipAmount)
    print("_________________________________")
    print("Total\t\t\t$", billTotal)
