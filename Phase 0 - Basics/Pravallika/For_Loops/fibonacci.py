#Write a program that uses a for loop to print the Fibonacci sequence up to the 10th term.
#Fibonacci sequence - first 10 terms
n_terms = 10
# First two terms
a, b = 0, 1
print("Fibonacci sequence (first 10 terms):")
for i in range(n_terms):
    print(a, end=" ")
    # Update values for next iteration
    a, b = b, a + b
print()  # new line at the end

'''Fibonacci sequence (first 10 terms):
   0 1 1 2 3 5 8 13 21 34''' 
