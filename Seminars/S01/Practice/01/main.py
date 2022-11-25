"""
Базовое задание:
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

var_x: str = 'Hello!'
var_y: int = 8
var_z: float = 14.14

print(var_x)
print(var_y)
print(var_z)

var_x = input('Введите текст: ')
var_y = int(input('Введите целое число: '))
var_z = float(input('Введите вещественное число: '))

print(var_x, type(var_x))
print(var_y, type(var_y))
print(var_z, type(var_z))