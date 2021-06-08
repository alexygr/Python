"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""


import random


def find_median(a):
    med = 0
    d = len(a)
    left = right = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] != a[j]:
                if a[i] >= a[j]:
                    left += 1
                if a[i] <= a[j]:
                    right += 1
        spam = right - left
        if spam < 0:
            spam = -spam
        elif spam == 0:
            return a[i]
        if d > spam:
            d = spam
            med = a[i]
        left = 0
        right = 0
    return med


MIN = 0
MAX = 9
SIZE = 21
array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(array)
print(sorted(array))
print(f"median = {find_median(array)}")
