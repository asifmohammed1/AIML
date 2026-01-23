#Write a function that returns the factorial of a given number.
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")  
    result = 1
    for i in range(1, n + 1):
        result *= i     
    return result
for i in range(11):
    print(f"{i}! = {factorial(i)}")
  

'''output:
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800'''
