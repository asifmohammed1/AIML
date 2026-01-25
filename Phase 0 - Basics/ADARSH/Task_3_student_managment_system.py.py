# PART 1: DATA STRUCTURE (LIST + DICT)

students = []   # list to store all students

# Function to add a new student
def add_student(name, age, email, grades):
    student = {
        "name": name,
        "age": age,
        "email": email,
        "grades": grades
    }
    students.append(student)
    return students

# PART 2: DATA MANIPULATION
# Find highest and lowest grade of a student
def highest_lowest_grade(grades):
    return max(grades), min(grades)

# Find student with highest average grade
def student_with_highest_average():
    highest_avg = 0
    best_student = ""

    for student in students:
        avg = sum(student["grades"]) / len(student["grades"])
        if avg > highest_avg:
            highest_avg = avg
            best_student = student["name"]

    return best_student, highest_avg

# Remove duplicate student names
def remove_duplicate_names(names):
    result = []
    for name in names:
        if name not in result:
            result.append(name)
    return result


# PART 3: STUDENT CLASS

class Student:
    def __init__(self, name, age, email, grades):
        self.name = name
        self.age = age
        self.email = email
        self.grades = grades

    # Add grade
    def add_grade(self, grade):
        self.grades.append(grade)

    # Calculate average grade
    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    # Display student information
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Average Grade:", self.get_average_grade())


# PART 4: SORTING & SEARCHING
# Sort students by average grade (descending)
def sort_students_by_average():
    return sorted(
        students,
        key=lambda s: sum(s["grades"]) / len(s["grades"]),
        reverse=True
    )


# Check if a student has a specific grade
def check_grade(student_name, grade):
    for student in students:
        if student["name"] == student_name:
            if grade in student["grades"]:
                return "Grade found"
            else:
                return "Grade not found"
    return "Student not found"


# BONUS FEATURES
# Palindrome check for student name
def is_palindrome(name):
    name = name.lower()
    return name == name[::-1]


# Leap year checker
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


# SAMPLE INPUT

add_student("Aman", 20, "aman@gmail.com", [80, 85, 90])
add_student("Neha", 21, "neha@gmail.com", [70, 75, 80])
add_student("Naman", 22, "naman@gmail.com", [88, 92, 90])

# Using Student class
s1 = Student("Ravi", 23, "ravi@gmail.com", [60, 70, 80])


# SAMPLE OUTPUT

print("All Students:", students)

print("Highest & Lowest Grades of Aman:",
      highest_lowest_grade(students[0]["grades"]))

print("Student with Highest Average:",
      student_with_highest_average())

names = ["Aman", "Neha", "Aman", "Ravi"]
print("After Removing Duplicates:", remove_duplicate_names(names))

print("Sorted Students by Average:", sort_students_by_average())

print("Check Grade:", check_grade("Neha", 75))

print("Is 'Naman' Palindrome?:", is_palindrome("Naman"))

print("Is 2004 a Leap Year?:", is_leap_year(2004))

print("\nStudent Class Info:")
s1.display_info()