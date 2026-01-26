#Problem Statement:
You are tasked with building a Student Management System to store, manipulate, and analyze student data. The system should be capable of handling a list of students and their associated data, including grades, contact details, and more. You must implement the following features:

class Student:
    def __init__(self, name, age, email, grades=(), birth_year=None):
        self.name, self.age, self.email = name, age, email
        self.grades = list(grades)
        self.birth_year = birth_year

    def avg(self): return sum(self.grades)/len(self.grades) if self.grades else 0
    def add_grade(self, g): self.grades.append(g)
    def info(self): print(f"{self.name} ({self.age}) | {self.email} | Avg: {self.avg():.1f}")

students = [
    Student("pravallika",   20, "pravallika@x.com", [85,90,78], 2004),
    Student("navya",     21, "navya@x.com", [92,88,95], 2003),
    Student("vicky", 19, "vicky@x.com", [76,82,88], 2005),
]
# Add student + grade
students.append(Student("uday", 20, "uday@x.com", [90,95,87]))
students[-1].add_grade(100)

# Highest average student
best = max(students, key=Student.avg)
print(f"Top student: {best.name} → {best.avg():.1f}")
# Sorted by average (descending)
for s in sorted(students, key=Student.avg, reverse=True):
    s.info()
# Has grade?
print("pravallika has 90?", 90 in students[0].grades)
       
#Bonus Feature:  
def is_palindrome(name):
    """Check if name is palindrome (case-insensitive, ignore spaces)."""
    cleaned = ''.join(name.lower().split())
    return cleaned == cleaned[::-1]
print("Is 'pravallika' a palindrome?", is_palindrome("pravallika"))
print("Is 'navya' a palindrome?", is_palindrome("navya"))
print("Is 'A man a plan a canal Panama' a palindrome?", is_palindrome("A man a plan a canal Panama"))
def is_leap_year(year):
    """Check if year is leap year using if conditions."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
# Test with student birth years
print("2004 is leap year?", is_leap_year(2004))  
print("2003 is leap year?", is_leap_year(2003))
print("2005 is leap year?", is_leap_year(2005))
# Integrate with Student class example
print("pravallika's birth year leap status:", is_leap_year(2004))

#output:Top student: uday → 93.0
uday (20) | uday@x.com | Avg: 93.0
navya (21) | navya@x.com | Avg: 91.7
pravallika (20) | pravallika@x.com | Avg: 84.3
vicky (19) | vicky@x.com | Avg: 82.0
pravallika has 90? True
#bonus
Is 'pravallika' a palindrome? False
Is 'navya' a palindrome? False
Is 'A man a plan a canal Panama' a palindrome? True
2004 is leap year? True
2003 is leap year? False
2000 is leap year? True
1900 is leap year? False
pravallika's birth year leap status: True
