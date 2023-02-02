"""
---
Базовое задание:
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

var_words = ['attribute', 'класс', 'функция', 'type']


def my_func(my_list):
    """
    Проверка на возможность записи в
    байтовом типе с маркировкой b\'.
    """
    for item in my_list:
        if not item.isascii():
            print(f'Слово "{item}" невозможно записать в '
                  f'байтовом типе с помощью маркировки b\'.')


my_func(var_words)
