"""
---
Базовое задание:
7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from itertools import count


def user_int_input():
    """
    Метод запрашивающий у пользователя ввести целое положительное число
    Если ввод целочисленный - возвращает это число, иначе повторяет запрос ввода.
    """
    while True:
        try:
            input_num = int(input('Введите целое положительное число: '))
            if input_num < 0:
                print('Ошибка ввода!')
            else:
                return input_num
        except ValueError:
            print('Ошибка ввода!')


def print_fact(input_num):
    """
    Функция выводит факторизацию.
    """
    for i in count(1):
        if i <= input_num - 1:
            print(i, end=' * ')
        else:
            break


def fact(input_n):
    """
    Функция расчёта факториала входящего числа.
    """
    result = 1
    for i in count(result):
        if i <= input_n:
            result *= i
        else:
            break
    yield result


print('Укажите число для расчёта факториала.')
user_num = user_int_input()
print(end=f'Факториал {user_num}! = ')
print_fact(user_num)
factorial = [print(end=f'{user_num} = {el}\n') for el in fact(user_num)]
