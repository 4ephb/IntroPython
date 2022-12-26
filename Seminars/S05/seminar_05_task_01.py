"""
---
Базовое задание:
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open('seminar_05_task_01.txt', 'w', encoding='utf-8') as file_obj:
    while True:
        new_string = input('Введите данные для записи в файл. '
                           'Для окончания ввода данных нажмите Enter:\n')
        if new_string == '':
            break
        file_obj.writelines(f'{new_string} \n')
file_obj.close()
