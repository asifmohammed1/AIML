#Write a function that takes a list of numbers and returns a new list with only the even numbers from the original list.
def get_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))
print(get_even_numbers([]))
print(get_even_numbers([10, 20, 30, 40]))


'''output[2, 4, 6, 8, 10]
         []
         [10, 20, 30, 40]'''
