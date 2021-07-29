def isPrimeNumber(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True


input = input("Enter the number : ")
num = int(input)
result = isPrimeNumber(num)
if result == True:
    print("The entered number {} is prime")
else:
    print("The entered number {} is not prime")

