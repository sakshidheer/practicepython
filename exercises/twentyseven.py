def generate_fizz_buzz_series(n):
    return ['Fizz' if i % 3==0 else 'Buzz' if i % 5 ==0 else i for i in range(1,n+1)]