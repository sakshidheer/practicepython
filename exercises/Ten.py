total = int(input("Enter number of items you want in list : "))

array = []
for i in range(0, total):
    array.append(int(input("Enter value")))

array.sort()

print("Largest number is {}".format(array[-1]))
