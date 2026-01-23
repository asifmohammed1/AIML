# creating a list using function

a = list(range(1, 101))
print(a)
even_numbers = []

# with this we can find even numbers in list and append it to even no empty list we just created

for i in a:
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

# function for finding maximum and minimum

def find_max_min(a):
    return max(a), min(a)
print(find_max_min(a))

# function that takes a list of strings and returns a new list with the lengths of each string.

def string_lengths(string):
    result = []
    for s in string:
        result.append(len(s))
    return result

# Example
strings = ["asif", "abhijeet", "adarsh","uday"]
print(string_lengths(strings))

# function that removes duplicate

def remove_duplicates(numbers):
    return list(set(numbers))

# Example
numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))

# task 1 part 2 dict

# 1. Function to return the key with the highest value
def highest_value_key(d):
    return max(d, key=d.get)


# 2. Function to return the average grade of students
def average_grade(grades):
    total = sum(grades.values())
    count = len(grades)
    return total / count


# 3. Function to add a new key-value pair to a dictionary
def add_pair(d, key, value):
    d[key] = value
    return d


# 4. Function to merge two dictionaries
# If a key is common, values are added
def merge_dicts(d1, d2):
    result = d1.copy()

    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result

# task 1 part 3

# 1. Multiplication table (1 to 10)
a = int(input('Enter a number for multiplication table : '))

for i in range(1, 11):
    print(a, "x", i, "=", a * i)


# 2. Sum of all numbers in a list
numbers = [1, 2, 3, 4, 5]
total = 0

for i in numbers:
    total += i

print("Sum =", total)


# 3. Right-angled triangle pattern of stars
rows = 5
for i in range(1, rows + 1):
    print("*" * i)


# 4. Fibonacci sequence up to 10th term
a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b


# task 1 part 4

# 1. Check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# 2. Check whether a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3. Check whether a string is a palindrome
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# 4. Check whether a year is a leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

# task 1 part 5

# 1. Function to check whether a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 2. Function to find factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 3. Function to find GCD of two numbers
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 4. Function to reverse a string
def reverse_string(text):
    return text[::-1]


# task 1 part 6

#  Person class
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)


#  Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_car_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)



#  Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount_percent):
        self.price = self.price - (self.price * discount_percent / 100)



#  BankAccount class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


