"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

MIN_ITEM = 1
MAX_ITEM = 100
SIZE = 9
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_n = 0
max_n = 0

for i in range(len(array)):
    if array[min_n] > array[i]:
        min_n = i
    if array[max_n] < array[i]:
        max_n = i

print(array)
array[min_n], array[max_n] = array[max_n], array[min_n]
print(array)
