"""
---
Базовое задание:
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('seminar_05_task_04_en.txt', 'r', encoding='utf-8') as file_obj:
    translated_list = []
    for line in file_obj:
        line = line.split(' ', 1)
        translated_list.append(translate[line[0]] + ' ' + line[1])

with open('seminar_05_task_04_ru.txt', 'w+', encoding='utf-8') as new_obj:
    new_obj.writelines(translated_list)
