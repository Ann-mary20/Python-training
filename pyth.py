def prime_factors(n):  
    factors = []
    i = 2  # Start with the smallest prime number
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors
num = int(input("Enter a number: "))
if num <= 1:
    print("Enter a number greater than 1.")
else:
    print(f"Prime factors of {num}: {prime_factors(num)}")
    
def fact(n):
    r= 1
    for i in range(2, n + 1):
        r *= i
    return r
n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} is: {fact(n)}")
def is_palindrome_number(num):
    return str(num) == str(num)[::-1]
num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
num = int(input("Enter number of terms: "))
if num <= 0:
    print("Please enter a positive number.")
else:
    fibonacci_series(num)
