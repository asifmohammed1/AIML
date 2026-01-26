#Write a function that takes a list of numbers and returns a new list with only the even numbers from the original list.
def even(input):
    enum=[]
    for i in input:
        if i%2==0:
            enum.append(i)
    return enum
input=[1,2,3,4,5,6,7,8]
print(even(input))
#output:[2,4,6,8]
#Write a function that finds the largest and smallest number in a given list of numbers.
def largest_smallest(input):
    large=max(input)
    small=min(input)
    return large,small
input=[1,2,3,4,5,67]
print(largest_smallest(input))
#output:(67,1)
#Write a program that takes a list of strings and returns a new list with the lengths of each string.
def stLength(input):
    le=[]
    for i in input:
        le.append(len(i))
    return le
input=["hello","hi","welcome"]    
print(stLength(input))
#output:[5,2,7]
#Given a list of integers, remove duplicates and return the updated list.
def reDuplicates(input):
    return list(set(input))
input=[1,2,3,4,4,5,5,6]
print(reDuplicates(input))
#output:[1,2,3,4,5,6]
#Write a function that accepts a dictionary and returns the key with the highest value.
def highestKey(input):
    for i in input:
        if input[i]==max(input.values()):
            return i
di={'a':10,'b':20,'c':5}  
print(highestKey(di))
#output: b 
#Given a dictionary of students and their grades, write a function that returns the average grade of all students.
def avgGrade(input):
    total=sum(input.values())   
    avg=total/len(input)   
    return avg
input={'stu1':85,'stu2':90,'stu3':78}
print(avgGrade(input))
#output: 84.33333333333333
#Write a program that takes a dictionary and adds a new key-value pair to it. The key will be a string, and the value will be a number.
def addKey(input,key,value):
    input[key]=value
    return input
input={'a':1,'b':2}
print(addKey(input,'c',3))
#output:{'a': 1, 'b': 2, 'c': 3}
#Write a function that merges two dictionaries. If the dictionaries have common keys, their values should be added together.
def mergeDist(dist1,dist2):
    for i in dist2:
        if i in dist1:
            dist1[i]+=dist2[i]
        else:
            dist1[i]=dist2[i]
    return dist1
dist={'a':1,'b':2}
dist2={'b':3,'c':4}
print(mergeDist(dist,dist2))
#output:{'a': 1, 'b': 5, 'c': 4}
#Write a program using a for loop to print the multiplication table of a given number (1 to 10).
n=int(input("enter"))
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
   '''output:enter2
            2X1=2
            2X2=4
            2X3=6
            2X4=8
            2X5=10
            2X6=12
            2X7=14
            2X8=16
            2X9=18
            2X10=20'''
#Use a for loop to iterate through a list of numbers and print the sum of all numbers.
l=[1,2,3,4,5,6,7]
s=0
for i in l:
    s=s+i
print(s)    
#output:28
#Write a program that uses a for loop to print a right-angled triangle pattern of stars (*).
n=5
for i in range(1,n+1):
    print("*"*i)
  '''output:
    *
    **
    ***
    ****
    *****'''
#Write a program that uses a for loop to print the Fibonacci sequence up to the 10th term.
n=10
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    output:0 1 1 2 3 5 8 13 21 34 
#Write a program that checks whether a number is positive, negative, or zero using if-else.
n=int(input("enter a number"))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("Zero") 
#output:enter a number-5
# negative'''
# Write a program that accepts a number and checks whether it is even or odd.
n=int(input("enter a number"))
if n%2==0:
    print("even")
else:
    print("odd")      
output:enter a number4
even
#Create a program that checks whether a given string is a palindrome
s=input("enter a string")
if s==s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
output:enter a string mam
palindrome     
#Write a program that takes a year as input and determines whether it is a leap year or not.
year=int(input("enter a year"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year") 
else:
    print("not a leap year")  
output:enter a year 2020
leap year 
#Write a function that takes a number as an argument and returns whether it is a prime number or not.
def prime(n):
    if n<=1:
        return "not a prime"
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return "not a prime"
    return "prime"   
num=int(input("enter a number"))
print(prime(num)) 
output:enter a number5
prime
#Write a function that returns the factorial of a given number.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a number"))    
print(factorial(n))   
output:enter a number5
       120
#Write a function that takes two numbers as arguments and returns their greatest common divisor (GCD).
def gcd(num1,num2):
    a,b=abs(num1),abs(num2)
    while b!=0:
        a,b=b,a%b
    return a
n1=int(input("enter n1:")) 
n2=int(input("enter n2:"))   
print(gcd(n1,n2))
output:enter n1:48
       enter n2:18
6
#Create a function that takes a string and returns the reverse of that string.
def reverse(str):
    reverse=str[::-1]
    return reverse
str="hello"
print(reverse(str))
output:olleh
#Create a Person class with the attributes name, age, and email. Implement a method to display the person’s details.
class person:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def display(self):
        print(f"Name:{self.name}")   
        print(f"Age:{self.age}")  
        print(f"Email:{self.email}")  
person1=person("dev",26,"dev@gmail.com")
person1.display()     
output:Name:dev
Age:26
Email:dev@gmail.com
#Create a Car class with attributes like make, model, year, and a method display_car_info that prints all the information of the car.
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(f"Make:{self.make}")   
        print(f"Model:{self.model}")  
        print(f"Year:{self.year}")  
Car1=Car("Toyota", "Corolla", 2022)
Car1.display()   
output:Make:Toyota
Model:Corolla
Year:2022
#Write a Book class that has a title, author, and price attributes. Implement a method to apply a discount to the book's price.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def discount(self, dis):
        if 0 <= dis <= 100:
            amt = self.price * (dis / 100)
            self.price = self.price - amt
        else:
            print("enter valid value")
book1 = Book("Python Basics", "John Doe", 500)
book1.discount(10)
print(book1.price)
output:450.0
#Create a BankAccount class with methods for depositing money, withdrawing money, and checking the balance.
class BankAccount:
    def __init__(self,bankHolder,balance):
        self.bankHolder=bankHolder
        self.balance=balance
    def Deposit(self,money):
        if money>0:
            self.balance=self.balance+money
            print(f"Deposited Money:{self.balance}")  
        else:
            print("enter valid amount")   
    def Withdraw(self,amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")  
    def CheckBalance(self):
         print(f"{self.bankHolder} Current balance: {self.balance}")
account = BankAccount("Dev", 1000)
account.Deposit(500)
account.Withdraw(300)
account.CheckBalance()
output:Deposited Money:1500
Withdrawn: 300
Dev Current balance: 1200
