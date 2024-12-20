'''2. Найти среднее среди положительных элементов матрицы А раз-
мером 5 × 7 .'''

from random import *

a = [[randint(1, 100) for i in range(7)] for i in range(5)]
print('Исходная матрица:\n')
for i in a:
    print(*i)
s = sum(sum(i) for i in a)
print(f'\nСумма всех элементов = {s}')