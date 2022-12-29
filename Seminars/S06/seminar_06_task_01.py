"""
---
Базовое задание:
1. Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать
замеры времени, оптимизировать, вновь выполнить замеры и
ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться.

Описания нужно делать в виде docstrings
"""

from timeit import timeit
from task_01 import func_1, func_2
from task_02 import first_pow, second_pow, third_pow, x, y
from task_03 import int_func_1, int_func_2, input_str
from task_04 import dec_to_bin_1, dec_to_bin_2

# task_01
print('\ntask_01.py - imported')
print(timeit('func_1(258369)', setup='from task_01 import func_1', number=100000))
print(timeit('func_2(258369)', setup='from task_01 import func_2', number=100000))

print('\ntask_01.py - globals')
func_1(258369)
print(timeit('func_1(258369)', globals=globals(), number=100000))  # +
func_2(258369)
print(timeit('func_2(258369)', globals=globals(), number=100000))

# task_02
print('\ntask_02.py - imported')
print(timeit('first_pow(x, y)',
             setup='from task_02 import first_pow, x, y',
             number=100000))
print(timeit('second_pow(x, y)',
             setup='from task_02 import second_pow, x, y',
             number=100000))
print(timeit('third_pow(x, y)',
             setup='from task_02 import third_pow, x, y',
             number=100000))

print('\ntask_02.py - globals')
first_pow(x, y)
print(timeit('first_pow(x, y)', globals=globals(), number=100000))  # +
second_pow(x, y)
print(timeit('second_pow(x, y)', globals=globals(), number=100000))
third_pow(x, y)
print(timeit('third_pow(x, y)', globals=globals(), number=100000))

# task_03
print('\ntask_03.py - imported')
print(timeit('int_func_1(input_str)',
             setup='from task_03 import int_func_1, input_str',
             number=100000))
print(timeit('int_func_2(input_str)',
             setup='from task_03 import int_func_2, input_str',
             number=100000))

print('\ntask_03.py - globals')
int_func_1(input_str)
print(timeit('int_func_1(input_str)', globals=globals(), number=100000))  # +
int_func_2(input_str)
print(timeit('int_func_2(input_str)', globals=globals(), number=100000))

# task_04
print('\ntask_04.py - imported')
print(timeit('dec_to_bin_1(42)',
             setup='from task_04 import dec_to_bin_1',
             number=100000))
print(timeit('dec_to_bin_2(42)',
             setup='from task_04 import dec_to_bin_2',
             number=100000))

print('\ntask_04.py - globals')
dec_to_bin_1(42)
print(timeit('dec_to_bin_1(42)', globals=globals(), number=100000))
dec_to_bin_2(42)
print(timeit('dec_to_bin_2(42)', globals=globals(), number=100000))  # +

"""
task_01.py
Поиск самой большой цифры в числе.
func_1
func_2

>>> task_01.py - imported
>>> 0.14182629995048046
>>> 0.34190819994546473

>>> task_01.py - globals
>>> 0.16226119990460575
>>> 0.24841420003212988

Указывая пространство имен при помощи globals=globals(),
наблюдается небольшая задержка по времени в методе func_2.
func_1 выполняется немного быстрее в обоих случаях, в
отличии от func_2. Встроенная функция max() не решила
проблему ускорения времени выполнения.


task_02.py
Возведение числа x в отрицательную степень y.
first_pow
second_pow
third_pow

>>> task_02.py - imported
>>> 0.019475999986752868
>>> 0.06552229996304959
>>> 0.03644339996390045

>>> task_02.py - globals
>>> 0.020705699920654297
>>> 0.06490829994436353
>>> 0.0421144999563694

first_pow существенно быстрее second_pow, third_pow в выполнении.
изначально метод first_pow оказался быстрее оптимизированного метода
third_pow. Встроенная функция pow() не решила проблему ускорения
времени выполнения.


task_03.py
Строка из слов в нижнем регистре, преобразуется
в строку в которой каждое слово начинается с
заглавной буквы.
int_func_1
int_func_2

>>> task_03.py - imported
>>> 0.10159710003063083
>>> 0.611208499991335

>>> task_03.py - globals
>>> 0.10128629999235272
>>> 0.6401558000361547

int_func_1 существенно быстрее int_func_2.
Решение было выбрано уже оптимизированным, поэтому
в данном случае видно, что оптимизированный способ
лучше.


task_04.py
Преобразование десятичного числа в двоичное.
dec_to_bin_1
dec_to_bin_2

>>> task_04.py - imported
>>> 0.1779936000239104
>>> 0.017892099916934967

>>> task_04.py - globals
>>> 0.19574679993093014
>>> 0.019796699983999133

dec_to_bin_2 существенно быстрее dec_to_bin_1.
Встроенная функция bin() решила проблему ускорения
времени выполнения (x10).

Заключение:
Не во всех случаях оптимизация памяти привела к лучшим результатам замеров времени.
Наблюдается, что оптимизированная реализация программного кода существенно может сократить
скорость работы программы в 2-10 раз.
"""
