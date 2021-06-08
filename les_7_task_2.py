"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge(left, right):
    c = [0] * (len(left) + len(right))
    i = j = n = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            c[n] = left[i]
            i += 1
            n += 1
        else:
            c[n] = right[j]
            j += 1
            n += 1
    while i < len(left):
        c[n] += left[i]
        i += 1
        n += 1
    while j < len(right):
        c[n] = right[j]
        j += 1
        n += 1
    return c


def merge_sort(data):
    if len(data) <= 1:
        return
    middle = len(data)//2
    left = data[0:middle]
    right = data[middle::]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for i in range(len(c)):
        data[i] = c[i]


MIN = 0
MAX = 50
SIZE = 10

array = [round(random.uniform(MIN, MAX), 2) for _ in range(SIZE)]
print(array)
merge_sort(array)
print(array)
