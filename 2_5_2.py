'''2. В массивах А размером 9 и В размером 7 заменить максимальные 
элементы на среднее арифметическое значение элементов, 
расположенных после максимального, в том массиве, для которого 
максимальный элемент расположен дальше от конца массива. 
Поиск максимального элемента осуществить в методе.'''

from operator import index
from random import *

a = [randint(1, 100) for i in range(9)]
b = [randint(1, 100) for i in range(7)]

print('Исходный массив а:\n', *a)
print('Исходный массив b:\n', *b, '\n')
print('='*40, '\n')

def max_el(x):
    m = x[0]
    for i in x:
        if i > m:
            m = i
    return m
l_a = len(a) - a.index(max_el(a)) - 1
l_b = len(b) - b.index(max_el(b)) - 1



sr = 0
if l_a == 0 and l_b == 0: 
    sr = max(max_el(a), max_el(b))
else: 
    if l_a > l_b:
        k = 0
        for i in range(a.index(max_el(a)), len(a)):
            k += a[i]
        sr = float(f'{k / l_a:.3f}')
    else:
        k = 0
        for i in range(b.index(max_el(b)), len(b)):
            k += b[i]
        sr = float(f'{k / l_b:.3f}')

a[a.index(max_el(a))] = sr
b[b.index(max_el(b))] = sr

print('Массив а после изменений:\n', *a)
print('Массив b после изменений:\n', *b)    