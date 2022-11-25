"""
Базовое задание:
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""
import math

var_x: str = 'Hello!'
var_y: int = 2
var_z: float = round(math.sqrt(var_y) * 10, 2)


# Вывод переменных
def print_all(a: str,
              b: int,
              c: float):
    print(a)
    print(b)
    print(c)


# Вывод переменных совместно с типом переменной
def print_all_w_types(a: str,
                      b: int,
                      c: float):
    print(a, "-", type(a).__name__)
    print(b, "-", type(b).__name__)
    print(c, "-", type(c).__name__)


print_all(var_x, var_y, var_z)

var_x = input('Введите текст: ')
var_y = int(input('Введите целое число: '))
var_z = float(input('Введите вещественное число: '))

print_all_w_types(var_x, var_y, var_z)
