def is_prime_number(num):
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

if __name__ == '__main__':
    input = input("Enter the number : ")
    num = int(input)
    result = is_prime_number(num)
    if result == True:
        print("The entered number {} is prime")
    else:
        print("The entered number {} is not prime")

