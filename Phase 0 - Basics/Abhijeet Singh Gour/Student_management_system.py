# List to store all students

students = [
    {
        "name": "Abhijeet",
        "age": 22,
        "email": "abhijeet123@gmail.com",
        "grades": [80, 85, 90]
    },
    {
        "name": "naman",
        "age": 21,
        "email": "naman123@gmail.com",
        "grades": [70, 75, 78]
    }
]

# Add a new student 

def add_student(student_list, name, age, email, grades):
    new_student = {
        "name": name,
        "age": age,
        "email": email,
        "grades": grades
    }
    student_list.append(new_student)
    return student_list

add_student(students,'adarsh',21,'adarsh123@gmail.com',[80,75,85])

print(students)

# To find highest and lowest grade of a student

def highest_and_lowest(grades):
    highest = grades[0]
    lowest = grades[0]

    for grade in grades:
        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade

    return highest, lowest

print(highest_and_lowest([80,70,85]))

# To find student with highest average grade

def student_with_highest_average(student_list):

    highest_avg = 0
    top_student = None

    for student in student_list:
        avg = sum(student["grades"]) / len(student["grades"])
        if avg > highest_avg:
            highest_avg = avg
            top_student = student["name"]

    return top_student

print(student_with_highest_average(students))

# To remove duplicates names 

def remove_duplicate_names(names):
    unique = []
    for name in names:
        if name not in unique:
            unique.append(name)
    return unique


names = ['anup','adarsh','abhijeet','anup','jayant']
print(remove_duplicate_names(names))

# To make a student class 

class student:
    def __init__(self, name, age, email, grades):
        self.name = name
        self.age = age
        self.email = email
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Average Grade:", self.average_grade())

s1 = student('anup',21,'anup123@gmail.com',[90,85])
s1.add_grade(80)
s1.info()

# To check a specifi grade

def check_grade(student, grade):
    for g in student.grades:
        if g == grade:
            return "Grade found"
    return "Grade not found"

print(check_grade(s1,90))
