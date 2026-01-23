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
