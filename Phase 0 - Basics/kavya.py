#Write a function that takes a list of numbers and returns a new list with only the even numbers from the original list.
'''def even(input):
    enum=[]
    for i in input:
        if i%2==0:
            enum.append(i)
    return enum
input=[1,2,3,4,5,6,7,8]
print(even(input))
output:[2,4,6,8]'''
#Write a function that finds the largest and smallest number in a given list of numbers.
'''def largest_smallest(input):
    large=max(input)
    small=min(input)
    return large,small
input=[1,2,3,4,5,67]
print(largest_smallest(input))
output:(67,1)'''
#Write a program that takes a list of strings and returns a new list with the lengths of each string.
'''def stLength(input):
    le=[]
    for i in input:
        le.append(len(i))
    return le
input=["hello","hi","welcome"]    
print(stLength(input))
output:[5,2,7]'''
#Given a list of integers, remove duplicates and return the updated list.
'''def reDuplicates(input):
    return list(set(input))
input=[1,2,3,4,4,5,5,6]
print(reDuplicates(input))
output:[1,2,3,4,5,6]'''
#Write a function that accepts a dictionary and returns the key with the highest value.
'''def highestKey(input):
    for i in input:
        if input[i]==max(input.values()):
            return i
di={'a':10,'b':20,'c':5}  
print(highestKey(di))
output: b '''
#Given a dictionary of students and their grades, write a function that returns the average grade of all students.
'''def avgGrade(input):
    total=sum(input.values())   
    avg=total/len(input)   
    return avg
input={'stu1':85,'stu2':90,'stu3':78}
print(avgGrade(input))
output: 84.33333333333333'''
#Write a program that takes a dictionary and adds a new key-value pair to it. The key will be a string, and the value will be a number.
'''def addKey(input,key,value):
    input[key]=value
    return input
input={'a':1,'b':2}
print(addKey(input,'c',3))
output:{'a': 1, 'b': 2, 'c': 3}'''
#Write a function that merges two dictionaries. If the dictionaries have common keys, their values should be added together.
'''def mergeDist(dist1,dist2):
    for i in dist2:
        if i in dist1:
            dist1[i]+=dist2[i]
        else:
            dist1[i]=dist2[i]
    return dist1
dist={'a':1,'b':2}
dist2={'b':3,'c':4}
print(mergeDist(dist,dist2))
output:{'a': 1, 'b': 5, 'c': 4}'''
#Write a program using a for loop to print the multiplication table of a given number (1 to 10).
'''n=int(input("enter"))
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
    output:enter2
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
'''l=[1,2,3,4,5,6,7]
s=0
for i in l:
    s=s+i
print(s)    
output:28'''
#Write a program that uses a for loop to print a right-angled triangle pattern of stars (*).
'''n=5
for i in range(1,n+1):
    print("*"*i)
    output:
    *
    **
    ***
    ****
    *****'''
#Write a program that uses a for loop to print the Fibonacci sequence up to the 10th term.
'''n=10
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    output:0 1 1 2 3 5 8 13 21 34 '''
#Write a program that checks whether a number is positive, negative, or zero using if-else.
'''n=int(input("enter a number"))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("Zero") 
#output:enter a number-5
# negative'''
# Write a program that accepts a number and checks whether it is even or odd.
'''n=int(input("enter a number"))
if n%2==0:
    print("even")
else:
    print("odd")      
output:enter a number4
even'''
#Create a program that checks whether a given string is a palindrome
'''s=input("enter a string")
if s==s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
output:enter a string mam
palindrome '''     
#Write a program that takes a year as input and determines whether it is a leap year or not.
'''year=int(input("enter a year"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year") 
else:
    print("not a leap year")  
output:enter a year 2020
leap year '''
#Write a function that takes a number as an argument and returns whether it is a prime number or not.
'''def prime(n):
    if n<=1:
        return "not a prime"
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return "not a prime"
    return "prime"   
num=int(input("enter a number"))
print(prime(num)) 
output:enter a number5
prime'''  
#Write a function that returns the factorial of a given number.
'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a number"))    
print(factorial(n))   
output:enter a number5
       120'''
#Write a function that takes two numbers as arguments and returns their greatest common divisor (GCD).
'''def gcd(num1,num2):
    a,b=abs(num1),abs(num2)
    while b!=0:
        a,b=b,a%b
    return a
n1=int(input("enter n1:")) 
n2=int(input("enter n2:"))   
print(gcd(n1,n2))
output:enter n1:48
       enter n2:18
6'''
#Create a function that takes a string and returns the reverse of that string.
'''def reverse(str):
    reverse=str[::-1]
    return reverse
str="hello"
print(reverse(str))
output:olleh'''
#Create a Person class with the attributes name, age, and email. Implement a method to display the person’s details.
'''class person:
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
Email:dev@gmail.com'''
#Create a Car class with attributes like make, model, year, and a method display_car_info that prints all the information of the car.
'''class Car:
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
Year:2022'''
#Write a Book class that has a title, author, and price attributes. Implement a method to apply a discount to the book's price.
'''class Book:
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
output:450.0'''
#Create a BankAccount class with methods for depositing money, withdrawing money, and checking the balance.
'''class BankAccount:
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
Dev Current balance: 1200'''
#Problem Statement1:
'''You are tasked with building a Student Management System to store, manipulate, and analyze student data. The system should be capable of handling a list of students and their associated data, including grades, contact details, and more. You must implement the following features:

Part 1: Data Structure Setup (Lists & Dictionaries)
Student List:
Create a list of students where each student is represented as a dictionary with the following keys:
name (string)
age (integer)
email (string)
grades (list of integers representing grades)

Add a New Student:
Implement a function that adds a new student to the list. The function should take the student's details as input and return the updated list.

Part 2: Data Manipulation (Lists & Functions)
Find Highest and Lowest Grades:
Write a function that takes a student's grades list and returns the highest and lowest grade.

Average Grade Calculation:
Implement a function that calculates the average grade for all students. The function should return the student with the highest average grade.

Remove Duplicates:
Given a list of student names, remove any duplicate names and return the updated list.

Part 3: Student Info (Functions, Classes & Dictionaries)

Student Class:
Create a Student class with the following attributes: name, age, email, and grades.
Implement a method within the class called get_average_grade that returns the average of the student's grades.

Method to Add Grades:
Implement a method within the Student class that allows you to add a grade to the student's grades list.

Display Student Information:
Implement a method that displays the student's name, age, email, and average grade.

Part 4: Sorting and Searching (For Loop & If Conditions)
Sorting Students by Average Grade:
Write a function that sorts the list of students based on their average grade in descending order.

Check for a Specific Grade:
Implement a function that checks if a given student has a particular grade. If so, return "Grade found," otherwise return "Grade not found."

Bonus (Optional):

Palindrome Check:
Write a function that checks if a student's name is a palindrome (the name reads the same forward and backward).
Leap Year Checker (if applicable):
Add a functionality that allows you to check whether the year of a student's birth year (given as an integer) is a leap year or not.

Requirements:

Use for loops to iterate over student data when required.
Implement if conditions to handle checking and decision-making, such as checking for duplicate names, grade presence, and leap years.
Use functions to separate out logic for better organization and readability.
Organize your code using classes for Student objects and methods.

Submission:

Provide the Python code for the Student Management System.
Include a sample input and output for each of the implemented functionalities.
Ensure the code is properly documented with comments to explain each function.'''
#source code
'''students_data = [
    {"name": "dev", "age": 22, "email": "dev@mail.com", "grades": [70, 65, 80]},
    {"name": "nan", "age": 19, "email": "nah@mail.com", "grades": [95, 100, 92]}
]

# Part 3: Student Class
class Student:
    def __init__(self, name, age, email, grades):
        self.name = name
        self.age = age
        self.email = email
        self.grades = grades if grades else []

    # Method to get average grade
    def get_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    # Method to add a grade
    def add_grade(self, grade):
        self.grades.append(grade)

    # Method to display student information
    def display_details(self):
        avg = self.get_average_grade()
        print(f"Name: {self.name:10} | Age: {self.age} | Email: {self.email:20} | Avg: {avg:.2f}")      

# Part 1: Function to add a new student
def add_new_student(student_list, name, age, email, grades):
    new_student = Student(name, age, email, grades)
    student_list.append(new_student)
    return student_list

# Part 2: Find highest and lowest grades
def high_low(grades):
    return max(grades), min(grades)

# Part 2: Calculate average and find highest average student
def get_top_student(students):
    if not students: 
        return None
    max_avg = 0
    max_student = None
    for student in students:
        current_avg = student.get_average_grade()
        if current_avg > max_avg:
            max_avg = current_avg
            max_student = student
    return max_student

# Part 3: Remove Duplicate names
def remove_duplicates(names):
    return list(set(names))

# Part 4: Sorting Students by Average Grade
def sort_students_by_grade(students):
    return sorted(students, key=lambda s: s.get_average_grade(), reverse=True)

# Part 5: Check for a Specific Grade
def check_grade(student, grade):
    if grade in student.grades:
        return "Grade found"
    return "Grade not found"

# Bonus: Palindrome Check
def is_palindrome(name):
    clean_name = name.lower().replace(" ", "")
    return clean_name == clean_name[::-1]

# Bonus: Leap Year Checker
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == "__main__":
    # 1. Setup Data & Part 1 Add Student
    my_students = []
    
    # Testing Add New Student
    add_new_student(my_students, "abc", 20, "abc@mail.com", [80, 90, 78])
    add_new_student(my_students, "dev", 22, "dev@mail.com", [70, 65, 80])
    add_new_student(my_students, "nan", 19, "nah@mail.com", [95, 100, 92])
    
    # 2. Testing Method to Add Grades (Part 3)
    print("Testing Add Grade")
    print(f"abc's grades before: {my_students[0].grades}")
    my_students[0].add_grade(95)
    print(f"abc's grades after:  {my_students[0].grades}\n")

    # 3. Student Details (Part 3 Display)
    print("Display All Students")
    for s in my_students:
        s.display_details()
    
    # 4. Highest and lowest grade (Part 2)   
    h, l = high_low(my_students[0].grades)
    print(f"Grade Manipulation")
    print(f"abc's Highest Grade: {h}, Lowest Grade: {l}")
    
    # 5. Remove duplicates (Part 2)
    duplicate_names = ["abc", "dev", "abc", "nan", "dev"]
    unique = remove_duplicates(duplicate_names)
    print(f"\n Remove Duplicates")
    print(f"Original: {duplicate_names}")
    print(f"Cleaned:  {unique}")
    
    # 6. Sorting Students (Part 4)
    print(f"\n Sorting Students by Average (Part 4)")
    sorted_s = sort_students_by_grade(my_students)
    for s in sorted_s:
        print(f"Ranked Student: {s.name:5} - Avg: {s.get_average_grade():.2f}")
    
    # 7. Top Student (Part 2 Result)    
    top = get_top_student(my_students)
    print(f"\n Top Performing Student")
    print(f"Top Student: {top.name} (Avg: {top.get_average_grade():.2f})")    
    
    # 8. Check specific grade and search (Part 4)
    print(f"\n-Check Specific Grade (Part 4)")
    print(f"Searching 'nan' for grade 100: {check_grade(my_students[2], 100)}")
    print(f"Searching 'dev' for grade 100: {check_grade(my_students[1], 100)}")
    
    # 9. Bonus Section
    print(f"\n Bonus Features ")
    print(f"Is 'nan' a palindrome? {is_palindrome('nan')}")
    print(f"Was 2000 a leap year? {is_leap_year(2000)}")
output:
Testing Add Grade
abc's grades before: [80, 90, 78]
abc's grades after:  [80, 90, 78, 95]

Display All Students
Name: abc        | Age: 20 | Email: abc@mail.com         | Avg: 85.75
Name: dev        | Age: 22 | Email: dev@mail.com         | Avg: 71.67
Name: nan        | Age: 19 | Email: nah@mail.com         | Avg: 95.67
Grade Manipulation
abc's Highest Grade: 95, Lowest Grade: 78

 Remove Duplicates
Original: ['abc', 'dev', 'abc', 'nan', 'dev']
Cleaned:  ['dev', 'abc', 'nan']

 Sorting Students by Average (Part 4)
Ranked Student: nan   - Avg: 95.67
Ranked Student: abc   - Avg: 85.75
Ranked Student: dev   - Avg: 71.67

 Top Performing Student
Top Student: nan (Avg: 95.67)

-Check Specific Grade (Part 4)
Searching 'nan' for grade 100: Grade found
Searching 'dev' for grade 100: Grade not found

 Bonus Features
Is 'nan' a palindrome? True
Was 2000 a leap year? True    '''
#Problem Statement2:
'''You need to build a Movie Rating System that allows users to add movies and rate them, calculate the average rating of all movies, and find the highest-rated movie.
Part 1: Data Structure Setup (Lists & Dictionaries)
Movie List:
Create a list of dictionaries where each dictionary represents a movie. Each movie should have:
title (string)
director (string)
year (integer)
rating (float)
Add a Movie:
Implement a function to add a new movie to the list. The function should accept the movie's details (title, director, year, rating) and return the updated list.
Part 2: Movie Rating and Average Calculation (Lists & Functions)
Add a Rating to a Movie:
Write a function that allows the user to add a rating to an existing movie. The function should take the movie title and the new rating as inputs.
Calculate Average Rating:
Write a function that calculates the average rating of all the movies in the list.
Find Highest-Rated Movie:
Implement a function that finds the movie with the highest rating and returns its title and rating.
Part 3: Sorting and Filtering (For Loops & If Conditions)
List Movies by Rating:
Write a function that lists all movies in the database, sorted by rating in descending order.
Filter Movies by Year:
Implement a function that filters and returns all movies released in a given year.
Bonus (Optional):
Check if Movie Title is Palindrome:
Implement a function that checks if a given movie title is a palindrome (the title reads the same forward and backward).
Submission:
Provide the Python code for the Movie Rating System.
Include sample input and output for each of the implemented functionalities.
Ensure the code is clean and properly documented.'''
#source code
'''movie_db = []

class Movie:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = float(rating)

    def display_info(self):
        print(f"Title: {self.title:20} | Director: {self.director:15} | Year: {self.year} | Rating: {self.rating}")

# Add a Movie 
def add_movie(movie_list, title, director, year, rating):
    new_movie = Movie(title, director, year, rating)
    movie_list.append(new_movie)
    return movie_list

# Rating and Average Calculation 
def update_rating(movie_list, title, new_rating):
    for movie in movie_list:
        if movie.title.lower() == title.lower():
            movie.rating = float(new_rating)
            return f"Rating for '{movie.title}' updated to {new_rating}."
    return "Movie not found."
#average Rating
def calculate_average_rating(movie_list):
    if not movie_list:
        return 0.0
    total = sum(movie.rating for movie in movie_list)
    return total / len(movie_list)
#highest rating
def find_highest_rated(movie_list):
    if not movie_list:
        return None
    highest_movie = movie_list[0]
    for movie in movie_list:
        if movie.rating > highest_movie.rating:
            highest_movie = movie
    return highest_movie.title, highest_movie.rating
# Sorting and Filtering 
def list_movies_by_rating(movie_list):
    return sorted(movie_list, key=lambda m: m.rating, reverse=True)
#Filter
def filter_movies_by_year(movie_list, year):
    filtered = []
    for movie in movie_list:
        if movie.year == year:
            filtered.append(movie)
    return filtered
# Palindrome Check 
def is_title_palindrome(title):
    clean_title = title.lower().replace(" ", "")
    return clean_title == clean_title[::-1]

if __name__ == "__main__":
    # 1. Setup Data 
    print(" 1. Testing Add Movie ")
    add_movie(movie_db, "Inception", "Christopher Nolan", 2010, 8.8)
    add_movie(movie_db, "Tenet", "Christopher Nolan", 2020, 7.4)
    add_movie(movie_db, "Memento", "Christopher Nolan", 2000, 8.4)
    print(f"Movies added: {len(movie_db)}\n")

    # 2. Update Rating 
    print("Testing Add Rating to Movie ")
    print(update_rating(movie_db, "Tenet", 7.8))
    
    # 3. Average and Highest 
    avg = calculate_average_rating(movie_db)
    title, score = find_highest_rated(movie_db)
    print(f"\nRating Analytics")
    print(f"Average System Rating: {avg:.2f}")
    print(f"Highest Rated Movie: {title} ({score})")

    # 4. Sorting 
    print(f"\nMovies Sorted by Rating ")
    for m in list_movies_by_rating(movie_db):
        m.display_info()

    # 5. Filtering 
    print(f"\nFiltering Movies by Year (2010)")
    results = filter_movies_by_year(movie_db, 2010)
    for r in results:
        print(f"Found: {r.title}")

    # 6. Bonus Palindrome
    print(f"\nBonus Palindrome Check")
    test_title = "Tenet"
    print(f"Is '{test_title}' a palindrome? {is_title_palindrome(test_title)}")
output:
1. Testing Add Movie 
Movies added: 3

Testing Add Rating to Movie
Rating for 'Tenet' updated to 7.8.

Rating Analytics
Average System Rating: 8.33
Highest Rated Movie: Inception (8.8)

Movies Sorted by Rating
Title: Inception            | Director: Christopher Nolan | Year: 2010 | Rating: 8.8
Title: Memento              | Director: Christopher Nolan | Year: 2000 | Rating: 8.4
Title: Tenet                | Director: Christopher Nolan | Year: 2020 | Rating: 7.8

Filtering Movies by Year (2010)
Found: Inception

Bonus Palindrome Check
Is 'Tenet' a palindrome? True    '''