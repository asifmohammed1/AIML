#Create a program that checks whether a given string is a palindrome (same forwards and backwards).
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

# Taking input from the user
string = input("Enter a string: ")

if is_palindrome(string):
    print("The given string is a Palindrome")
else:
    print("The given string is NOT a Palindrome")

'''output:
   Enter a string: madam in eden im adam
   The given string is a Palindrome
   Enter a string: iiiii
   The given string is a Palindrome'''
