#Write a function that accepts a dictionary and returns the key with the highest value.
# first create the dictionary
scores = {"pravulu": 85, "navya": 92, "lallitha": 78, "vicky": 95}
# Define the function
def get_key_with_max_value(d):
    if not d:
        return None
    return max(d, key=d.get)
# call it and print
print(get_key_with_max_value(scores))

#output: vicky
