def is_num_armstrong(num):
    if num < 1:
        return False
    if num < 10:
        return True
    
    

def get_order(num):
    digits = 0
    while num !=0:
        num = num // 10
        digits +=1
    return digits
