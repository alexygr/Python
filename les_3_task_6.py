"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

MIN_ITEM = 1
MAX_ITEM = 100
SIZE = 9
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_n = 0
max_n = 0
sum_n = 0

for i in range(SIZE):
    if array[min_n] > array[i]:
        min_n = i
    if array[max_n] < array[i]:
        max_n = i

print(array)
print(f"Минимвльный элемент {min_n} - {array[min_n]}.\nМаксимальнй элемент {max_n} - {array[max_n]}.")

if min_n > max_n:
    min_n, max_n = max_n, min_n

for i in range(min_n+1, max_n):
    sum_n += array[i]

print(f"Сумма елементов между ними = {sum_n}")
