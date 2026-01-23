#Write a program that takes a list of strings and returns a new list with the lengths of each string.
def get_string_lengths(strings):
    return [len(s) for s in strings]
print(get_string_lengths(["Pravallika", "Lallitha", "2026"]))

#output:[10, 8, 4]
