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


for size in (1000, 10000, 100000):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    print(timeit.timeit('f_number1(array)', number=1000, globals=globals()))
    print(timeit.timeit('f_number2(array)', number=1000, globals=globals()))
    print(timeit.timeit('f_number3(array)', number=1000, globals=globals()))
    cProfile.run('f_number1(array)')
    cProfile.run('f_number2(array)')
    cProfile.run('f_number3(array)')
    print()

"""
11.286574314000001
0.11608091700000145
8.661563123
         3261 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.000    0.000    0.012    0.012 les_4_task_1.py:17(f_number1)
     1000    0.011    0.000    0.011    0.000 les_4_task_1.py:9(in_array)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1256    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:34(f_number2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1008 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.000    0.000    0.009    0.009 les_4_task_1.py:49(f_number3)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
     1004    0.009    0.000    0.009    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



12.014693799000003
0.1238936069999994
9.261866782999995
         3219 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
        1    0.000    0.000    0.011    0.011 les_4_task_1.py:17(f_number1)
     1000    0.011    0.000    0.011    0.000 les_4_task_1.py:9(in_array)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1214    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:34(f_number2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1006 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.000    0.000    0.009    0.009 les_4_task_1.py:49(f_number3)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
     1002    0.009    0.000    0.009    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



11.437565186
0.1280241139999987
9.245911569
         3241 function calls in 0.011 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
        1    0.000    0.000    0.011    0.011 les_4_task_1.py:17(f_number1)
     1000    0.010    0.000    0.011    0.000 les_4_task_1.py:9(in_array)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1236    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:34(f_number2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1008 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.000    0.000    0.009    0.009 les_4_task_1.py:49(f_number3)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
     1004    0.009    0.000    0.009    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""