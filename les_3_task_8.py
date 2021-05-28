"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""


LINE_SIZE = 5
COL_SIZE = 4
matrix = [[0]*LINE_SIZE for i in range(COL_SIZE)]

for i in range(len(matrix)):
    line = list(map(int, input(f'Ведите {i+1}-й ряд из {LINE_SIZE - 1}-х чисел: ').split()))
    for j in range(len(matrix[0]) - 1):
        matrix[i][j] = line[j]
        matrix[i][len(matrix[0])-1] += line[j]

print('-' * 7 * len(matrix[0]))
for line in matrix:
    for el in line:
        print(f'{el:>6}', end='|')
    print('\n', '------+' * len(matrix[0]), sep='')
