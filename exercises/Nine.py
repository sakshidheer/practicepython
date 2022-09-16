def findIfNumOdd(num):
    num = int(input)
    remainder =  num % 2 ==0
    if remainder:
        print("The entered number is even")
    else:
        print("The entered number is odd")

input = input("Please enter the number : ")

findIfNumOdd(input)


