from collections import Counter

cool_list: list = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
count: Counter = Counter(cool_list)
print(count)
# Counter({1: 2, 2: 1, 3: 1, 4: 1, 5: 3, 6: 2})

# Strings
print(Counter("aaaaabbbbbccccc"))
# Counter({'a': 5, 'b': 5, 'c': 5})