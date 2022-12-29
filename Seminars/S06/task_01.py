"""
Семинар 01
---
Базовое задание:
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в
числе. Для решения используйте цикл while и арифметические операции.
"""


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
