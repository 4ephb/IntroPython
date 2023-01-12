"""
Тестируемые классы их экземпляры и методы из задач с 1 по 8 семинары.
"""
from itertools import count


# ------------------------------------------------------------------------------(1)
# Семинар: 3 / Базовое задание: 3
def my_func(arg_1, arg_2, arg_3):
    """
    Функция принимает на вход три числа и
    возвращает сумму наибольших двух аргументов.
    (сумма всех чисел) - (минимальное число)
    """
    return arg_1 + arg_2 + arg_3 - min([arg_1, arg_2, arg_3])


# ------------------------------------------------------------------------------(2)
# Семинар: 3 / Дополнительное задание: 3

def diff_two_numb(input_list):
    """
    Метод находит разницу между максимальным и минимальным
    значением дробной части элементов.
    :return: result
    """
    result = [round(i % 1, 2) for i in input_list if i % 1 != 0]
    return max(result) - min(result)


# ------------------------------------------------------------------------------(3)
# Семинар: 3 / Базовое задание: 6

def int_func(word):
    """
    Функция принимает на вход строку состоящую из слов с
    маленькой буквы и возвращает слово с заглавной буквы.
    """
    return word.title()


# ------------------------------------------------------------------------------(4)
# Семинар: 4 / Базовое задание: 4

def duplicates_in_list(input_list):
    """
    Метод определяет элементы списка, не имеющие повторений.
    """
    result = [el for el in input_list if input_list.count(el) == 1]
    return result


# ------------------------------------------------------------------------------(5)
# Семинар: 8 / Базовое задание: 3

class DivisionByZero(Exception):
    """
    Класс-исключение, обрабатывающий ситуацию деления на нуль.
    """

    def __init__(self, text):
        self.text = text


def division_by_zero_1(div, den):
    """
    Метод 1 обрабатывающий ситуацию деления на нуль.
    """
    try:
        if den == 0:
            raise DivisionByZero('Деление на ноль невозможно!')
    except DivisionByZero:
        return 'Деление на ноль невозможно!'
    else:
        return f'{div} / {den} = {div / den}'


def division_by_zero_2(div, den):
    """
    Метод 2 обрабатывающий ситуацию деления на нуль.
    """
    if den == 0:
        raise DivisionByZero('Деление на ноль невозможно!')
    return f'{div} / {den} = {div / den}'


# ------------------------------------------------------------------------------(6)
# Семинар: 4 / Базовое задание: 6

def int_gen(start_int, finish_int):
    """
    Метод генерирующий целые числа, начиная с указанного
    """
    result = []
    for i in count(start_int):
        if i <= finish_int:
            result.append(i)
        else:
            break
    return result


# ------------------------------------------------------------------------------(7)
# Семинар: 8 / Базовое задание: 2

class Cell:
    """
    Базовый класс Cell.
    """

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'{self.quantity * "*"}'

    def __add__(self, other):
        return f'Сумма клеток = ({self.quantity + other.quantity})'

    def __sub__(self, other):
        return 'Разность отрицательна, поэтому операция не выполняется' \
            if (self.quantity - other.quantity) <= 0 \
            else f'Разность клеток = ({self.quantity - other.quantity})'

    def __mul__(self, other):
        return f'Умножение клеток = ({self.quantity * other.quantity})'

    def __truediv__(self, other):
        return f'Деление клеток = ({self.quantity // other.quantity})'

    def make_order(self, cells_in_row):
        """
        Метод принимает экземпляр класса и количество ячеек в ряду.
        Данный метод позволяет организовать ячейки по рядам.
        :return: ******\n ****\n ** ...
        """
        row = []
        for _ in range(self.quantity // cells_in_row):
            row.append('*' * cells_in_row)
        if self.quantity % cells_in_row != 0:
            row.append('*' * (self.quantity % cells_in_row))
        return '\\n '.join(row)


# ------------------------------------------------------------------------------(8)
# Семинар: 7 / Базовое задание: 2

class Road:
    """
    Аттрибуты класса
    """

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, as_mass, as_height):
        """
        Метод возвращает результат перемножения атрибутов с
        атрибутами класса
        """
        print(f'{int(self._length * self._width * as_mass * as_height / 1000)} т')

    def plug(self):
        """заглушка"""
