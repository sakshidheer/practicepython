def conert_min_to_sec(min):
    return min *60

input = input("Enter the number in min : ")
min = int(input)

print("The {} mins in seconds is {}".format(min,conert_min_to_sec(min)))