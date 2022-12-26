"""
---
Базовое задание:
5. Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна подсчитывать
сумму чисел в файле и выводить ее на экран.
"""

with open('seminar_05_task_05.txt', 'w+', encoding='utf-8') as file_obj:
    file_obj.write(input('Введите числа через пробел: '))

with open('seminar_05_task_05.txt', 'r+', encoding='utf-8') as file_obj:
    print(f'Сумма чисел в файле: {sum(map(int, file_obj.read().split()))}')
