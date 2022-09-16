def conertMinToSec(min):
    return min *60

input = input("Enter the number in min : ")
min = int(input)

print("The {} mins in seconds is {}".format(min,conertMinToSec(min)))