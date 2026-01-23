#Write a function that takes a number as an argument and returns whether it is a prime number or not.
#prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")
  

'''output:
 Enter a number: 29
 29 is a Prime Number
