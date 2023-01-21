carType = 0
washCost = 0.00
Wax = "Selected"
waxCost = 0
Shine = "Selected"
shineCost = 0
Rust = "Selected"
rustCost = 0
unselect = "Not Selected"

cartype = input("Select Vehicle Type (Car, Pickup, or Minivan): ")

if cartype == "Car":
    carType = 1
    washCost = 6.00
    waxCost = 1
    shineCost = 2
    rustCost = 3
elif cartype == "Pickup":
    carType = 2
    washCost = 9.00
    waxCost = 2
    shineCost = 4
    rustCost = 3
elif cartype == "Minivan":
    carType = 3
    washCost = 8.00
    waxCost = 2
    shineCost = 3
    rustCost = 3
else:
    print("Error")
    carType = 0

if carType != 0:
    wax = input("Do you want a wax (Y/N)? ")
else:
    print("Invalid Entry")
if wax == "Y":
    waxCost = waxCost
elif wax == "N":
    waxCost = 0
    Wax = unselect
else:
    print("Invalid Entry")

if carType != 0:
    shine = input("Do you want a Wheel Shine (Y/N)? ")
else:
    print("Invalid Entry")
if shine == "Y":
    shineCost = shineCost
elif shine == "N":
    shineCost = 0
    Shine = unselect
else:
    print("Invalid Entry")

if carType != 0:
    rust = input("Do you want a Rust Inhibitor (Y/N)? ")
else:
    print("Invalid Entry")

if rust == "Y":
    rustCost = rustCost
elif rust == "N":
    rustCost = 0
    Rust = unselect
else:
    print("Invalid Entry")

print("")
print("_" * 35)
print("Vehicle Type: \t\t" + cartype)
print("Basic Wash: \t\t" + "$", washCost)
print("Wax: \t\t\t" + Wax)
print("Wheel Shine: \t\t" + Shine)
print("Rust Inhibitor: \t" + Rust)
print("_" * 35)
total = washCost + waxCost + shineCost + rustCost
print("Total Cost: \t\t" + "$", total)
