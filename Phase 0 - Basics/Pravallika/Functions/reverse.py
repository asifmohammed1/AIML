#Create a function that takes a string and returns the reverse of that string.
def reverse_string(s):
    return s[::-1]
words = ["hello", "python", "navya", "Pravallika", "12345", ""]
for word in words:
    print(f"'{word}' reversed → '{reverse_string(word)}'")


'''output:
'hello' reversed → 'olleh'
'python' reversed → 'nohtyp'
'navya' reversed → 'ayvan'
'Pravallika' reversed → 'akillavarP'
'12345' reversed → '54321'
'' reversed → ''
