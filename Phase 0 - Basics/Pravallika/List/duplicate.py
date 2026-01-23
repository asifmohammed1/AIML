#Given a list of integers, remove duplicates and return the updated list.
def remove_duplicates(numbers):
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(remove_duplicates([1, 2, 3, 2, 4, 1, 5, 3, 6, 2]))
# Output: [1, 2, 3, 4, 5, 6]
