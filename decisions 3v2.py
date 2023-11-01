cost = int(input("Please Enter Cost Of Groceries: "))

#total = eval(cost)
coupon = 0

if cost < 10:
    coupon = 0
elif 10<cost<60:
    coupon = ((cost)*.08)
elif 60<cost<150:
    coupon = ((cost)*.10)
elif 150<cost<210:
    coupon = ((cost)*.12)
else:
    coupon = ((cost)*.14)

val = 0

val = (coupon/cost)*100

print('You win a discount coupon of ' , coupon , ' ,',  val, '% of your purchase')
