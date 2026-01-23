#1 List Tasks

#Write a function that takes a list of numbers and returns a new list with only the even numbers from the original list.

#define the function
def get_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))
print(get_even_numbers([]))

'''output:[2,4,6,8]
          []'''


#Write a function that finds the largest and smallest number in a given list of numbers.

def find_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)
print(find_min_max([42.5, 17.3, 99.9, 3.14]))


#output:(3.14, 99.9)


#Write a program that takes a list of strings and returns a new list with the lengths of each string.

def get_string_lengths(strings):
    return [len(s) for s in strings]
print(get_string_lengths(["Pravallika", "Lallitha", "2026"]))

#output:[10, 8, 4]


#Given a list of integers, remove duplicates and return the updated list.

def remove_duplicates(numbers):
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(remove_duplicates([1, 2, 3, 2, 4, 1, 5, 3, 6, 2]))
# Output: [1, 2, 3, 4, 5, 6]




#2 Dictionary Tasks

#Given a dictionary of students and their grades, write a function that returns the average grade of all students.

# create Dictionary
students = {
    "pravullu": 85,
    "navya": 92,
    "lalli": 78,
    "vicky": 95
}
def average_grade(grades_dict):
    if not grades_dict:
        return None
    total = sum(grades_dict.values())
    count = len(grades_dict)
    return total / count
print(average_grade(students))

#output:87.5



#Write a function that accepts a dictionary and returns the key with the highest value.

# first create the dictionary
scores = {"pravulu": 85, "navya": 92, "lallitha": 78, "vicky": 95}
# Define the function
def get_key_with_max_value(d):
    if not d:
        return None
    return max(d, key=d.get)
# call it and print
print(get_key_with_max_value(scores))

#output: Vicky


#Write a program that takes a dictionary and adds a new key-value pair to it. The key will be a string, and the value will be a number.

def add_new_entry(my_dict, key1, value1, key2, value2):
    if not isinstance(key1, str) or not isinstance(key2, str):
        print("Error: Keys must be strings!")
        return my_dict
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        print("Error: Values must be numbers!")
        return my_dict
    
    my_dict[key1] = value1
    my_dict[key2] = value2
    return my_dict

# Now both get added
updated = add_new_entry(students, "navya", 78, "lallitha", 80)
print(updated)
# Output: {'pravullu': 85, 'vicky': 92, 'navya': 78, 'lallitha': 80}


#Write a function that merges two dictionaries. If the dictionaries have common keys, their values should be added together.

#create dictionaries
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 15, "c": 5, "d": 40}
#define the function
def merge_dicts_with_sum(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
print(merge_dicts_with_sum(d1, d2))

#output:{'a': 10, 'b': 35, 'c': 35, 'd': 40}



#3 For Loops Tasks

#Write a program that uses a for loop to print the Fibonacci sequence up to the 10th term.

#Fibonacci sequence - first 10 terms
n_terms = 10
# First two terms
a, b = 0, 1
print("Fibonacci sequence (first 10 terms):")
for i in range(n_terms):
    print(a, end=" ")
    # Update values for next iteration
    a, b = b, a + b
print()  # new line at the end

'''Fibonacci sequence (first 10 terms):
   0 1 1 2 3 5 8 13 21 34'''



#Write a program using a for loop to print the multiplication table of a given number (1 to 10).

#Multiplication table (1 to 10)
number = int(input("Enter a number to see its multiplication table: "))
print(f"\nMultiplication Table of {number}:")
print("-" * 25)
for i in range(1, 11):
    print(f"{number} × {i:2d} = {number * i:3d}")

'''output:Enter a number to see its multiplication table: 9

Multiplication Table of 9:
-------------------------
9 ×  1 =   9
9 ×  2 =  18
9 ×  3 =  27
9 ×  4 =  36
9 ×  5 =  45
9 ×  6 =  54
9 ×  7 =  63
9 ×  8 =  72
9 ×  9 =  81
9 × 10 =  90'''



#Use a for loop to iterate through a list of numbers and print the sum of all numbers.

numbers = [7, 12, 4, 19, 8, 25]
total = 0
for n in numbers:
    total += n
print(f"Sum of {numbers} = {total}\n")

#output:Sum of [7, 12, 4, 19, 8, 25] = 75



#Write a program that uses a for loop to print a right-angled triangle pattern of stars (*).
#Right-angled triangle of stars
rows = int(input("Enter number of rows for the triangle: "))
print()
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()   # move to next line

'''output:Enter number of rows for the triangle: 7

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * '''



#4 If Conditions Tasks


#Write a program that accepts a number and checks whether it is even or odd.

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

'''output:Enter an integer: 7
   7 is Odd'''



#Write a program that takes a year as input and determines whether it is a leap year or not.

#Leap Year Checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")

'''output:
  Enter a year: 9000
  000 is NOT a Leap Year
  
  Enter a year: 2026
  2026 is NOT a Leap Year

  Enter a year: 2000
  2000 is a Leap Year'''




#Write a program that checks whether a number is positive, negative, or zero using if-else.

#sourcecode
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print("The number is Zero")

'''output:
  Enter a number: 100
  100 is Positive'''




#Create a program that checks whether a given string is a palindrome (same forwards and backwards).

def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

# Taking input from the user
string = input("Enter a string: ")

if is_palindrome(string):
    print("The given string is a Palindrome")
else:
    print("The given string is NOT a Palindrome")

'''output:
   Enter a string: madam in eden im adam
   The given string is a Palindrome
   Enter a string: iiiii
   The given string is a Palindrome'''





#5 Functions TaSKS


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
 29 is a Prime Number'''




#Create a function that takes a string and returns the reverse of that string.

def reverse_string(s):
    return s[::-1]
words = ["hello", "python", "navya", "Pravallika", "12345", ""]
for word in words:
    print(f"'{word}' reversed → '{reverse_string(word)}'")


'''output:
'hello' reversed → 'olleh'
'python' reversed → 'nohtyp'
'navya' reversed → 'ayvan'
'Pravallika' reversed → 'akillavarP'
'12345' reversed → '54321'
'' reversed → '' '''




#6 Class Tasks


#Create a Person class with the attributes name, age, and email.

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def display_details(self):
        print("Person Details:")
        print(f"  Name  : {self.name}")
        print(f"  Age   : {self.age}")
        print(f"  Email : {self.email}")
        print("-" * 30)
p1 = Person("Pravallika", 22, "pravallika@gmail.com")
p1.display_details()
p2 = Person("navya", 25, "navyadadi1999@gmail.com")
p2.display_details()


'''output:
  Person Details:
  Name  : Pravallika
  Age   : 22
  Email : pravallika@gmail.com
  ------------------------------
  Person Details:
  Name  : navya
  Age   : 25
  Email : navyadadi1999@gmail.com
  -----------------------



#Create a Car class with attributes like make, model, year, and a method display_car_info that prints all the information of the car.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_car_info(self):
        print("Car Information:")
        print(f"  Make  : {self.make}")
        print(f"  Model : {self.model}")
        print(f"  Year  : {self.year}")
        print("-" * 30)
car1 = Car("Toyota", "Innova Crysta", 2023)
car1.display_car_info()
car2 = Car("Tesla", "Model Y", 2025)
car2.display_car_info()

'''output:
Car Information:
  Make  : Toyota
  Model : Innova Crysta
  Year  : 2023
------------------------------
Car Information:
  Make  : Tesla
  Model : Model Y
  Year  : 2025
------------------------------'''



#Write a Book class that has a title, author, and price attributes. Implement a method to apply a discount to the book's price.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            print("Invalid discount percentage!")
            return
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        print(f"Discount of {percentage}% applied!")
        print(f"New price: ₹{self.price:.2f}")
    def display_info(self):
        print("Book Details:")
        print(f"  Title  : {self.title}")
        print(f"  Author : {self.author}")
        print(f"  Price  : ₹{self.price:.2f}")
        print("-" * 30)


'''output:
Book Details:
  Title  : Python for Beginners
  Author : John Smith
  Price  : ₹599.00
------------------------------
Discount of 15% applied!
New price: ₹509.15
Book Details:
  Title  : Python for Beginners
  Author : John Smith
  Price  : ₹509.15
------------------------------'''




#Create a BankAccount class with methods for depositing money, withdrawing money, and checking the balance.

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"New balance: ₹{self.balance:.2f}")
    
    def check_balance(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: ₹{self.balance:.2f}")
        print("-" * 30)
acc = BankAccount("Pravallika", "123456789012", 5000.00)
acc.check_balance()
acc.deposit(2500.50)
acc.withdraw(1800)
acc.withdraw(7000)      # should fail
acc.check_balance()


'''output:
Account Holder : Pravallika
Account Number : 123456789012
Current Balance: ₹5000.00
------------------------------
₹2500.50 deposited successfully.
New balance: ₹7500.50
₹1800.00 withdrawn successfully.
New balance: ₹5700.50
Insufficient balance!
Account Holder : Pravallika
Account Number : 123456789012
Current Balance: ₹5700.50
------------------------------'''






