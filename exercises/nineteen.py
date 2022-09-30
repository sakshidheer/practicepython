def get_square_root(num):
    if num < 1:
        raise ValueError("Value cannot be negative")
    return pow(num,0.5)