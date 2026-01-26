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
students_data = [
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
        print(f"Name: {self.name:10}  Age: {self.age}  Email: {self.email:20}  Avg: {avg:.2f}")      

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
'''output:
Testing Add Grade
abc's grades before: [80, 90, 78]
abc's grades after:  [80, 90, 78, 95]

Display All Students
Name: abc         Age: 20  Email: abc@mail.com         | Avg: 85.75
Name: dev         Age: 22  Email: dev@mail.com         | Avg: 71.67
Name: nan         Age: 19  Email: nah@mail.com         | Avg: 95.67
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
Was 2000 a leap year? True   
#Problem Statement2:'''