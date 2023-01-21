# Define constant list.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def main() :
   print("The original data for all functions is: ", ONE_TEN)

# Demonstrate swapping the first and last element.
   data = list(ONE_TEN)
   swapFirstLast(data)
   print("After swapping first and last: ", data)

def swapFirstLast(data) :
   if len(data) == 0 :
      return 

   temp = data[0]
   data[0] = data[len(data) - 1]
   data[len(data) - 1] = temp
