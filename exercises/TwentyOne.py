def is_num_armstrong(num):
    if num < 1:
        return False
    if num < 10:
        return True
    order = get_order(num)
    sum = 0
    temp = num
    while temp > 0:
        sum += pow(temp % 10, order)
        temp = temp // 10
    return sum == num

def get_order(num):
    digits = 0
    while num !=0:
        num = num // 10
        digits +=1
    return digits
