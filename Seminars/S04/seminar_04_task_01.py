"""
---
Базовое задание:
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.

# python seminar_04_task_01.py 164 500 17875

"""

from sys import argv


def calculate_salary():
    """
    Функция расчета заработной платы сотрудника.
    (выработка в часах*ставка в час) + премия
    """
    try:
        salary = float(hours_worked) * float(hourly_cost) + float(salary_bonus)
        print(f'\nВыработка в часах: {hours_worked}\n'
              f'Ставка в час:  {hourly_cost}\n'
              f'Премия: {salary_bonus}\n'
              f'Заработная плата: {salary}')
    except ValueError:
        print('Неверные параметры! Повторите попытку!\n'
              'Пример: python seminar_04_task_01.py 164 500 17875')


script_name, hours_worked, hourly_cost, salary_bonus = argv

calculate_salary()
