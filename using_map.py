def upper(string_for : str):
    return string_for.upper()
    
string_list: list = list(map(upper, ['python', 'javascript']))
print(string_list)
# ['PYTHON', 'JAVASCRIPT']

# Convert string in list of numbers
ints_list: list = list(map(int, "1234567"))
print(ints_list)
# [1, 2, 3, 4, 5, 6, 7]