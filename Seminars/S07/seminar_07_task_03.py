"""
---
Базовое задание:
3. Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на
реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """
    Базовый класс.
    """

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def plug_1(self):
        """заглушка-1"""

    def plug_2(self):
        """заглушка-2"""


class Position(Worker):
    """
    Дочерний класс.
    """

    def get_full_name(self):
        """
        Метод возвращает имя и фамилию одной строкой.
        """
        return self.name + ' ' + self.surname

    def get_total_income(self):
        """
        Метод возвращает сумму оклада с премией.
        """
        return sum(self._income.values())


employee_01 = Position('Владимир', 'Иванов', 'дизайнер', {'wage': 100000, 'bonus': 25000})
print(f'{employee_01.get_full_name()} ({employee_01.position}) - '
      f'{employee_01.get_total_income()} руб.')

employee_02 = Position('Олег', 'Поправкин', 'редактор', {'wage': 80000, 'bonus': 15000})
print(f'{employee_02.get_full_name()} ({employee_02.position}) - '
      f'{employee_02.get_total_income()} руб.')
