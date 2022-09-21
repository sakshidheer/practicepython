def find_if_num_odd(num):
    num = int(input)
    remainder =  num % 2 ==0
    if remainder:
        print("The entered number is even")
    else:
        print("The entered number is odd")

input = input("Please enter the number : ")

find_if_num_odd(input)


