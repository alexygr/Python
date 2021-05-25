"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""


import  random

MIN_ITEM = 1
MAX_ITEM = 100
SIZE = 10
array = [random.randint(MIN_ITEM, MAX_ITEM+1) for _ in range(SIZE)]

print(array)
for ind in range(2):
    i = SIZE - 1
    while i > ind:
        if array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
        i -= 1

print(array[0], array[1])
