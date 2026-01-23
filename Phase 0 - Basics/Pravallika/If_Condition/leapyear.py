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
  
