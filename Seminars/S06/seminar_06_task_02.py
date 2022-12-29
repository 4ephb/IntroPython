"""
---
Базовое задание:
2. Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать
замеры памяти, оптимизировать, вновь выполнить замеры и
ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться.

Описания нужно делать в виде docstrings
"""

from memory_profiler import profile

x, y = 2, -2
input_str: str = 'каждое слово должно начинаться с заглавной буквы.'


# task_01.py
@profile
def func_1(num):
    """
    Первоначальное решение через while.
    """
    max_num = 0
    while num > 0:
        number = num % 10
        num //= 10
        if number > max_num:
            max_num = number
    return max_num


print(func_1(258369))


@profile
def func_2(num):
    """
    Оптимизированное решение с функцией max.
    """
    max_num = 0
    while num:
        number = num % 10
        max_num = max(max_num, number)
        num = num // 10
    return max_num


print(func_2(258369))


# task_02.py
@profile
def first_pow(num_x, num_y):
    """
    Первоначальное решение возведения в
    степень с помощью оператора *.
    """
    return 1 / (num_x * abs(num_y))


print(first_pow(x, y))


@profile
def second_pow(num_x, num_y):
    """
    Первоначальное решение возведения в степень без
    оператора *, предусматривающая использование цикла.
    """
    result = 1
    for i in range(0, num_y * -1):
        result = result / num_x
        i += 1
    return result


print(second_pow(x, y))


@profile
def third_pow(num_x, num_y):
    """
    Оптимизированное решение возведения в
    степень с помощью функции pow.
    """
    return pow(num_x, num_y)


print(third_pow(x, y))


# task_03.py
@profile
def int_func_1(input_word):
    """
    Первоначальное решение с помощью функции title.
    """
    return input_word.title()


print(int_func_1(input_str))


@profile
def int_func_2(input_word):
    """
    Решение без помощи функции title.
    """
    return ' '.join(s[:1].upper() + s[1:] for s in input_word.split(' '))


print(int_func_2(input_str))


# task_04.py
@profile
def dec_to_bin_1(input_num):
    """
    Первоначальное решение через while.
    """
    bin_num = ""
    while input_num != 0:
        bin_num = str(input_num % 2) + bin_num
        input_num //= 2
    if not bin_num:
        bin_num = "0"
    return bin_num


print(dec_to_bin_1(42))


@profile
def dec_to_bin_2(input_num):
    """
    Оптимизированное решение с помощью функции bin.
    """
    return bin(input_num)


print(dec_to_bin_2(42))

"""
task_01.py
Поиск самой большой цифры в числе.
func_1 - 29 вхождений строк
func_2 - 28 вхождений строк


task_02.py
Возведение числа x в отрицательную степень y.
first_pow - 2 вхождения строк
second_pow - 11 вхождений строк
third_pow - 2 вхождения строк


task_03.py
Строка из слов в нижнем регистре, преобразуется
в строку в которой каждое слово начинается с
заглавной буквы.
int_func_1 - 2 вхождения строк
int_func_2 - 18 вхождений строк


task_04.py
Преобразование десятичного числа в двоичное.
dec_to_bin_1 - 23 вхождений строк
dec_to_bin_2 - 2 вхождения строк

Заключение:
В каждом случае выделялось памяти 23.0 MiB.
Инкремент памяти в каждом случае 0.0 MiB.
Проблем с памятью нет. Всё в пределах нормы.
Существенных ускорений не обнаружено.

"""
