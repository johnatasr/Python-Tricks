

new_list = [i for i in range(10)]
print(new_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [x**2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def cool_function(a):
    return (a + 5) / 2
    
my_formula = [cool_function(i) for i in range(10)]
print(my_formula)
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]

by_filter = [i for i in range(20) if i % 2 == 0]
print(by_filter)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]