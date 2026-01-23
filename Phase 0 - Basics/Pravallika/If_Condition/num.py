#Write a program that checks whether a number is positive, negative, or zero using if-else.
#sourcecode
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print("The number is Zero")

'''output:
  Enter a number: 100
  100 is Positive'''
