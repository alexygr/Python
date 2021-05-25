"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""


LINE_SIZE = 5
COL_SIZE = 4
matrix = [[0]*LINE_SIZE for i in range(COL_SIZE)]

for i in range(COL_SIZE):
    line = list(map(int, input(f'Ведите {i+1}-й ряд из {LINE_SIZE - 1}-х чисел: ').split()))
    for j in range(LINE_SIZE - 1):
        matrix[i][j] = line[j]
        matrix[i][LINE_SIZE-1] += line[j]

print('-' * 7 * LINE_SIZE)
for line in matrix:
    for el in line:
        print(f'{el:>6}', end='|')
    print('\n', '------+' * LINE_SIZE, sep='')
