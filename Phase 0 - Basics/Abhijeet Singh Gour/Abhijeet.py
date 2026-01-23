
# Write a function that takes a list of numbers and returns a new list with only the even numbers from the original list.

def even_list(nums):
    lis = []
    for i in nums:
        if i %2==0:
            lis.append(i)
        
    return lis

lis1 = [1,2,3,4,5,6,7,8,9]
print('list task 1 -',even_list(lis1))


# Write a function that finds the largest and smallest number in a given list of numbers.

def largest_smallest(nums):
    largest = nums[0]
    smallest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num 
    
    return largest,smallest


lis2 = [2,3,4,0,10,11]
print('list task 2 -',largest_smallest(lis2))


# Write a program that takes a list of strings and returns a new list with the lengths of each string.

def len_string(strings):
    lenght = []
    for word in strings:
        lenght.append(len(word))
    
    return lenght

str = ['abhijeet','singh','gour']
print('list task 3 -',len_string(str))
    
# Given a list of integers, remove duplicates and return the updated list.

def remove_duplicates(nums):
    lis = []
    for num in nums:
        if num not in lis:
            lis.append(num)
    return lis

n1 = [1,1,2,3,4,4,5,6,7]
print('list task 4 -',remove_duplicates(n1))

# Write a function that accepts a dictionary and returns the key with the highest value.

def key_with_highest_value(d):
    keys = list(d.keys())

    highest_key = keys[0]
    highest_value = d[highest_key]

    for key in keys:
        if d[key] > highest_value:
            highest_value = d[key]
            highest_key = key

    return highest_key

dic1 = {'abhi': 10 , 'aman': 20 , 'adarsh': 30 , 'rahul': 50}

print('dic task 1 -',key_with_highest_value(dic1))

# Given a dictionary of students and their grades, write a function that returns the average grade of all students.

def average(d):
    k = 0
    v = 0
    for value in d.values():
        k += value
        v += 1 
    
    return k/v

dic2 = {'abhi': 10 ,'aman': 20 , 'adarsh': 30 ,'rahul': 50}

print('dic task 2 -',average(dic2))


# Write a program that takes a dictionary and adds a new key-value pair to it. The key will be a string, and the value will be a number.

def add_key_value(d,key,value):
    d[key] = value
    
    return d

dic3 = {'a': 1 , 'b': 2, 'c': 4}

print('dic task 3 -',add_key_value(dic3, 'd',3))

# Write a function that merges two dictionaries. If the dictionaries have common keys, their values should be added together.

def merge_dic(d1,d2):
    result = d1.copy()

    for key,values in d2.items():
        if key in result:
            result[key] += values
        
        else:
            result[key] = values
    return result

dic4 = {'a':10 , 'b':20, 'c':30 }
dic5 = {'c':10 , 'd':40, 'e':45 }

print('dic task 4 -',merge_dic(dic4,dic5))


# Write a program using a for loop to print the multiplication table of a given number (1 to 10).

a = int(input('Enter a number for multiplication table : '))

for i in range(1,11) :
    print(f'{a} x {i} =',a * i) 

# Use a for loop to iterate through a list of numbers and print the sum of all numbers.

def sum (lis):
    total = 0

    for num in lis:
        total = total + num

    return total


l = [1,2,3,4,5,6]

print('Loop task 2 -',sum(l))


# Write a program that uses a for loop to print a right-angled triangle pattern of stars (*).

def stars(n):

    for i in range (1,n+1):
        print('*' * i)

print('loop task 3 -')
stars(5)

# Write a program that uses a for loop to print the Fibonacci sequence up to the 10th term.

a = 0
b = 1

print('loop task 4 -')
for i in range (10):
    print(a)
    c = a + b
    a = b
    b = c

# Write a program that checks whether a number is positive, negative, or zero using if-else.

print ('condition task 1 -')

num = int(input("Enter a number to check +ve -ve and 0 : "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Write a program that accepts a number and checks whether it is even or odd.

print('condition task 2 -')

num1 = int(input('Enter a number to check even or odd: '))

if num1 %2==0:
    print('Even')

else:
    print('odd')

# Create a program that checks whether a given string is a palindrome (same forwards and backwards).

w = input("Enter a word to chekc palindrome or not: ")

if w == w[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Write a program that takes a year as input and determines whether it is a leap year or not.

print ('condition task 4 -')

year = int(input("Enter a year to find leap year or not : "))

if year % 400 == 0:
    print("Leap year")

elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")

else:
    print("Not a leap year")

# Write a function that takes a number as an argument and returns whether it is a prime number or not.

def prime_or_not(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
print('fun task 1-')
print(prime_or_not(4))
print(prime_or_not(6))
print(prime_or_not(5))
print(prime_or_not(3))

# Write a function that returns the factorial of a given number.

def factorial(n):
    if n < 0:
        return "Invalid input"

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print('fun task 2 -',factorial(8))

# Write a function that takes two numbers as arguments and returns their greatest common divisor (GCD).

def greatest_common_divisor(a, b):
    smallest = min(a, b)

    for i in range(smallest, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print('fun task 3 -',greatest_common_divisor(8,12))

# Create a function that takes a string and returns the reverse of that string.

def reverse_string(s):
    reversed_str = ""

    for char in s:
        reversed_str = char + reversed_str

    return reversed_str

print('fun task 4 -', reverse_string('abhijeetsinghgour'))
print(reverse_string('cricket'))


# Create a Person class with the attributes name, age, and email. Implement a method to display the person’s details.

class person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def info(self):
        print('Name of the person is:', self.name)
        print('age of the person is:', self.age)
        print('email of the person is:', self.email)


a = person('Abhijeet',20,'abhijeet123@gmail.com')

print('class task 1 -')
a.info()

# Create a Car class with attributes like make, model, year, and a method display_car_info that prints all the information of the car.

class car:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    
    def car_info(self):
        print('model of the car is', self.model)
        print('yearr of the car is', self.year)

obj = car("sedan" , 2020)
obj1 = car('SUV', 2024)

print('class task 2 -')

obj.car_info()
obj1.car_info()

# Write a Book class that has a title, author, and price attributes. Implement a method to apply a discount to the book's price.

class book:
    def __init__(self, title, author, price):

        self.title = title
        self.author = author
        self.price = price

    def discount(self, discount_percent):

        discount_amount = self.price * (discount_percent / 100)
        self.price = self.price - discount_amount

obj2 = book('Atomic habits','James clear', 350)

print('class task 3 -')

print('title of book -',obj2.title)
print('auther of book -',obj2.author)
print('price of book -',obj2.price)
obj2.discount(10)
print('the discount price is -',obj2.price)

# Create a BankAccount class with methods for depositing money, withdrawing money, and checking the balance.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current balance:", self.balance)

account = BankAccount(1000)
print('class task 4 -')
account.check_balance()
account.deposit(500)
account.check_balance()
account.withdraw(200)
account.check_balance()
