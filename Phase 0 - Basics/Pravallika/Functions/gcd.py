#Write a function that takes two numbers as arguments and returns their greatest common divisor (GCD).
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a
pairs = [(48, 18), (54, 24), (17, 13), (100, 75), (0, 56)]
for x, y in pairs:
    print(f"GCD({x}, {y}) = {gcd(x, y)}")

'''output:
GCD(48, 18) = 6
GCD(54, 24) = 6
GCD(17, 13) = 1
GCD(100, 75) = 25
GCD(0, 56) = 56'''
