#Write a program that takes a dictionary and adds a new key-value pair to it. The key will be a string, and the value will be a number.
def add_new_entry(my_dict, key1, value1, key2, value2):
    if not isinstance(key1, str) or not isinstance(key2, str):
        print("Error: Keys must be strings!")
        return my_dict
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        print("Error: Values must be numbers!")
        return my_dict
    
    my_dict[key1] = value1
    my_dict[key2] = value2
    return my_dict

# Now both get added
updated = add_new_entry(students, "navya", 78, "lallitha", 80)
print(updated)
# Output: {'pravullu': 85, 'vicky': 92, 'navya': 78, 'lallitha': 80}
