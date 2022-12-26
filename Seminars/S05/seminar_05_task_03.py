"""
---
Базовое задание:
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии
этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open('seminar_05_task_03.txt', 'r', encoding='utf-8') as file_obj:
    low_salary = [line.split()[0] for line in file_obj if float(line.split()[1]) < 20000]
    print(f'Сотрудники с окладом менее 20 тысяч: {len(low_salary)} чел. '
          f'\n[{", ".join(low_salary)}]\n', end='\n')

with open('seminar_05_task_03.txt', 'r', encoding='utf-8') as file_obj:
    average_salary = [float(line.split()[1]) for line in file_obj]
    print(f'Средняя величина дохода сотрудников: {sum(average_salary) / len(average_salary)}')
