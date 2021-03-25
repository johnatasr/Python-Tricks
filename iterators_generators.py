import sys
import time

l = list(range(1000))

l_iterator = iter(l)

print('Size normal list: ', sys.getsizeof(l))
print('Size iterator list: ', sys.getsizeof(l_iterator))


print(next(l_iterator))
print(next(l_iterator))
print(next(l_iterator))


def not_ger_range():
    numbers: list = []
    for number in range(100):
        numbers.append(number)
        time.sleep(0.1)


def ger_range():
    for number in range(100):
        yield number
        time.sleep(0.1)

run_ger = ger_range()
not_ger = not_ger_range()

print(sys.getsizeof(run_ger)) # 120
print(sys.getsizeof(not_ger)) # 16


#Create a normal list
nice_list = [n for n in range(100)]
# Gerator list
nice_list = (n for n in range(100))

