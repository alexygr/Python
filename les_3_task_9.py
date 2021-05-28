"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random


def f_max_of_min(m):
    row = len(m)
    col = len(m[0])
    max_item = 0
    for i in range(0, col):
        min_item = m[i][0]
        for j in range(0, row):
            if min_item > m[j][i]:
                min_item = m[j][i]
        if i == 0:
            max_item = min_item
        print(f'{min_item} ', end=' ')
        if max_item < min_item:
            max_item = min_item
    print()
    return max_item


ROW = 5
COL = 10
MIN = 1
MAX = 100
mtr = [[random.randint(MIN, MAX) for _ in range(ROW)] for _ in range(COL)]
print(*mtr, sep='\n')
print('-' * 50)
print(f_max_of_min(mtr))
