"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import timeit
import cProfile
import random


def in_array(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    else:
        return -1


def f_number1(arr):
    c_array = [[], []]
    max_n = 0

    for item in range(len(arr)):
        c_i = in_array(c_array[0], arr[item])
        if c_i > -1:
            c_array[1][c_i] += 1
            if c_array[1][max_n] < c_array[1][c_i]:
                max_n = c_i
        else:
            c_array[0].append(arr[item])
            c_array[1].append(1)

    return c_array[0][max_n], c_array[1][max_n]


def f_number2(arr):
    counter = {}
    frequency = 1
    num = None
    for item in arr:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    return num, counter[num]


def f_number3(arr):
    n_max = 0
    number = None
    for item in arr:
        if n_max < arr.count(item):
            n_max = arr.count(item)
            number = item
    return number, n_max


MIN_ITEM = 1
MAX_ITEM = 1000
SIZE = 1000


for size in (300, 600, 1200):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    print(timeit.timeit('f_number1(array)', number=1000, globals=globals()))
    cProfile.run('f_number1(array)')
    print()

# этот код самый медленный.
# 100  - 1.621662385
#          1117 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 les_4_task_1.py:17(f_number1)
#       300    0.001    0.000    0.001    0.000 les_4_task_1.py:9(in_array)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       301    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       512    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 300 - 4.8892617089999995
#          2093 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 les_4_task_1.py:17(f_number1)
#       600    0.005    0.000    0.005    0.000 les_4_task_1.py:9(in_array)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#       601    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       888    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 1200 - 15.217764893000002
#          3771 function calls in 0.015 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.001    0.001    0.015    0.015 les_4_task_1.py:17(f_number1)
#      1200    0.014    0.000    0.014    0.000 les_4_task_1.py:9(in_array)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#      1201    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1366    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

for size in (1000, 10000, 100000):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    print(timeit.timeit('f_number2(array)', number=1000, globals=globals()))
    cProfile.run('f_number2(array)')
    print()

# этот код самый быстрый
# 1000 - 0.11690250699999893
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:34(f_number2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 10_000 - 1.5321513350000018
#          4 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 les_4_task_1.py:34(f_number2)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100_000 - 15.333282399000002
#          4 function calls in 0.015 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.015    0.015    0.015    0.015 les_4_task_1.py:34(f_number2)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

for size in (1000, 2000, 3000):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    print(timeit.timeit('f_number3(array)', number=1000, globals=globals()))
    cProfile.run('f_number3(array)')
    print()

# этот код чуть быстрее 1 варианта
# 1000 - 8.870725913000001
#          1008 function calls in 0.010 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.000    0.000    0.010    0.010 les_4_task_1.py:49(f_number3)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#      1004    0.010    0.000    0.010    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2000 - 34.31578084900001
#          2009 function calls in 0.034 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.034    0.034 <string>:1(<module>)
#         1    0.000    0.000    0.034    0.034 les_4_task_1.py:49(f_number3)
#         1    0.000    0.000    0.034    0.034 {built-in method builtins.exec}
#      2005    0.034    0.000    0.034    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 3000 - 76.78127062600001
#          3009 function calls in 0.077 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.077    0.077 <string>:1(<module>)
#         1    0.001    0.001    0.077    0.077 les_4_task_1.py:49(f_number3)
#         1    0.000    0.000    0.077    0.077 {built-in method builtins.exec}
#      3005    0.076    0.000    0.076    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
