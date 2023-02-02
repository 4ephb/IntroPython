"""
---
Базовое задание:
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

var_words = ['разработка', 'администрирование', 'protocol', 'standard']


def str_byte_str(my_list):
    """
    Преобразование из строкового представления в
    байтовое и обратно в строковое.
    """
    new_list = []
    print('В байты:')
    for item in my_list:
        byte_items = item.encode('utf-8')
        print(f'\t{byte_items} - {type(byte_items)}')
        new_list.append(byte_items)
    print('\nВ строку:')
    for i in new_list:
        string_items = i.decode('utf-8')
        print(f'\t{string_items} - {type(string_items)}')


str_byte_str(var_words)
