"""
---
Базовое задание:
3. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZero(Exception):
    """
    Класс-исключение, обрабатывающий ситуацию деления на нуль.
    """

    def __init__(self, text):
        self.text = text


def division_by_zero(div, den):
    """
    Метод обрабатывающий ситуацию деления на нуль.
    """
    try:
        if den == 0:
            raise DivisionByZero('Деление на ноль невозможно!')
    except DivisionByZero as err:
        print(err)
    else:
        print(f'{div} / {den} = {div / den}')


divider = int(input('Введите делимое: '))
denominator = int(input('Введите делитель: '))
division_by_zero(divider, denominator)

# division_by_zero(15, 6)
# division_by_zero(15, 0)
