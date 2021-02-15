import sys

list_by_range = range(0, 10000)
print(sys.getsizeof(list_by_range))
# 48


list_by_lc = [x for x in range(0, 10000)]
print(sys.getsizeof(list_by_lc))
# 87632 it more huge