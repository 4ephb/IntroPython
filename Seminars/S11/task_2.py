"""
---
Базовое задание:
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов (не используя!!! методы encode и decode) и
определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

var_b_format = [b'class', b'function', b'method']


def my_func(my_list):
    """
    Проверка типа, содержимого и длины переменной.
    """
    for item in my_list:
        print(f'\tТип переменной: {type(item)}')
        print(f'\tСодержимое переменной: {item}')
        print(f'\tДлина переменной: {len(item)}\n')


print('Байтовый формат:\n')
my_func(var_b_format)