#Write a program using a for loop to print the multiplication table of a given number (1 to 10).
#Multiplication table (1 to 10)
number = int(input("Enter a number to see its multiplication table: "))
print(f"\nMultiplication Table of {number}:")
print("-" * 25)
for i in range(1, 11):
    print(f"{number} × {i:2d} = {number * i:3d}")

'''output:Enter a number to see its multiplication table: 9

Multiplication Table of 9:
-------------------------
9 ×  1 =   9
9 ×  2 =  18
9 ×  3 =  27
9 ×  4 =  36
9 ×  5 =  45
9 ×  6 =  54
9 ×  7 =  63
9 ×  8 =  72
9 ×  9 =  81
9 × 10 =  90'''
  
