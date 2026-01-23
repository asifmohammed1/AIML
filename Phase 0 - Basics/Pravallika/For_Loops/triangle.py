#Write a program that uses a for loop to print a right-angled triangle pattern of stars (*).
#Right-angled triangle of stars
rows = int(input("Enter number of rows for the triangle: "))
print()
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()   # move to next line

'''output:Enter number of rows for the triangle: 7

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * '''
