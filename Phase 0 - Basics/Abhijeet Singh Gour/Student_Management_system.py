# List to store all students
students = [
    {
        "name": "Abhijeet",
        "age": 22,
        "email": "abhijeet123@gmail.com",
        "grades": [80, 85, 90]
    },
    {
        "name": "Naman",
        "age": 21,
        "email": "naman123@gmail.com",
        "grades": [70, 75, 78]
    }
]

# Add a new student
def add_student(student_list, name, age, email, grades):
    student_list.append({
        "name": name,
        "age": age,
        "email": email,
        "grades": grades
    })

add_student(students, "Adarsh", 21, "adarsh123@gmail.com", [80, 75, 85])

print("\nStudents:")
for s in students:
    print(s["name"], "-", s["grades"])


# Highest and lowest grade
def highest_and_lowest(grades):
    highest = grades[0]
    lowest = grades[0]

    for g in grades:
        if g > highest:
            highest = g
        if g < lowest:
            lowest = g

    return highest, lowest

high, low = highest_and_lowest([80, 70, 85])
print("\nHighest grade:", high)
print("Lowest grade:", low)


# Student with highest average
def student_with_highest_average(student_list):
    highest_avg = 0
    top_student = ""

    for student in student_list:
        avg = sum(student["grades"]) / len(student["grades"])
        if avg > highest_avg:
            highest_avg = avg
            top_student = student["name"]

    return top_student

print("\nStudent with highest average:", student_with_highest_average(students))


# Remove duplicate names
def remove_duplicate_names(names):
    unique = []
    for name in names:
        if name not in unique:
            unique.append(name)
    return unique

names = ['anup', 'adarsh', 'abhijeet', 'anup', 'jayant']
print("\nUnique names:", remove_duplicate_names(names))


# Student class
class Student:
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
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Average grade:", self.average_grade())


s1 = Student("Anup", 21, "anup123@gmail.com", [90, 85])
s1.add_grade(80)
s1.info()


# Check specific grade
def check_grade(student, grade):
    for g in student.grades:
        if g == grade:
            return "Grade found"
    return "Grade not found"

print("\nGrade check:", check_grade(s1, 90))

# Outputs:

# Students:
# Abhijeet - [80, 85, 90]
# Naman - [70, 75, 78]
# Adarsh - [80, 75, 85]

# Highest grade: 85
# Lowest grade: 70

# Student with highest average: Abhijeet

# Unique names: ['anup', 'adarsh', 'abhijeet', 'jayant']

# Name: Anup
# Age: 21
# Email: anup123@gmail.com
# Average grade: 85.0

# Grade check: Grade found
