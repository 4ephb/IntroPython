"""
---
Базовое задание:
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("seminar_05_task_02.txt", "r", encoding='utf-8') as file_obj:
    file_lines = file_obj.readlines()
    print(f'Количество строк в файле: {len(file_lines)}')
    n_line: int = 0
    for line in file_lines:
        words: int = 0
        for i in line.split():
            words += 1
        print(f'В {n_line + 1} строке количество слов: {words}.  # {file_lines[n_line]}', end='\b')
        n_line += 1
file_obj.close()
