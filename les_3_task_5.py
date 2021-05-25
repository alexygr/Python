"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

MIN_ITEM = -100
MAX_ITEM = 100
SIZE = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
el = 0

for i in range(SIZE):
    if 0 > array[i] > array[el] or array[el] > 0:
        el = i

print(array)
print(f"Максимальный отрицательный элемент - {array[el]}, позицию в массиве {el}")
