#Write a function that merges two dictionaries. If the dictionaries have common keys, their values should be added together.
#create dictionaries
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 15, "c": 5, "d": 40}
#define the function
def merge_dicts_with_sum(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
print(merge_dicts_with_sum(d1, d2))

#output:{'a': 10, 'b': 35, 'c': 35, 'd': 40}
