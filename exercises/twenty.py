def is_num_prime(num):
    if num < 1:
        return False
    is_prime = True
    for index in range(2, num):
        if num % index == 0:
            is_prime = False
            break
    return is_prime

