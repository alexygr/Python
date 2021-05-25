"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random


def in_array(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    else:
        return -1


MIN_ITEM = 1
MAX_ITEM = 100
SIZE = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

c_array = [[], []]

for item in range(SIZE):
    c_i = in_array(c_array[0], array[item])
    if c_i > -1:
        c_array[1][c_i] += 1
    else:
        c_array[0].append(array[item])
        c_array[1].append(1)

max_n = 0
for el in c_array[1]:
    if max_n < el:
        max_n = el

# print(array)

for item in range(len(c_array[0])):
    if c_array[1][item] == max_n:
        print(f'Число {c_array[0][item]}, Встречается {c_array[1][item]} раз')
