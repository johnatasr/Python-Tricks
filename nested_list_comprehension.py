nested_list = [[j for j in range(3)] for i in range(4)]
print(nested_list)
#  [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

nested_list2 = [value
      for sublist in m
      for value in sublist]

print(nested_list2)
# [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]