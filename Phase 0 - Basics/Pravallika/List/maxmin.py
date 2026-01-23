#Write a function that finds the largest and smallest number in a given list of numbers.
def find_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)
print(find_min_max([42.5, 17.3, 99.9, 3.14]))


#output:(3.14, 99.9)
