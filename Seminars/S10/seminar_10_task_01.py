"""
---
Базовое задание:
01. Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ.
"""


class AttrValidation:
    """
    Класс, проверяющий атрибуты.
    """

    def __init__(self):
        self.my_attr = None

    def __set__(self, instance, value):
        if int != type(value) and float != type(value):
            raise TypeError(f'Значение {self.my_attr} не является числом. '
                            f'Введите положительное число.')
        if value <= 0:
            raise ValueError(f'Значение {self.my_attr} должно быть больше нуля. '
                             f'Введите положительное число.')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def plug(self):
        """заглушка"""


# ---------------------------------------------------------------------------------------(1)
# Семинар: 7 / Базовое задание: 2

class Road:
    """
    Класс Road
    """
    # Атрибуты класса объявляем дескрипторами
    _length = AttrValidation()
    _width = AttrValidation()

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


# Without Error
road_1 = Road(20, 5000)
road_1.mass(25, 5)

# TypeError
road_2 = Road('двадцать', 5000)
road_2.mass(25, 5)


# ValueError
# road_3 = Road(-20, 5000)
# road_3.mass(25, 5)


# ---------------------------------------------------------------------------------------(2)
# Семинар: 8 / Базовое задание: 2

class Cell:
    """
    Базовый класс Cell.
    """
    # Атрибуты класса объявляем дескрипторами
    quantity = AttrValidation()

    def __init__(self, quantity):
        self.quantity = quantity

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


print('\nСоздаем объекты клеток')
cell1 = Cell(30)  # Without Error
cell2 = Cell('двадцать пять')  # TypeError
cell3 = Cell(-10)  # ValueError
cell4 = Cell(15)

print(cell1)
print(cell2)
print(cell3)
print(cell4)

print('\nСкладываем')
print(cell1 + cell2)

print('\nВычитаем')
print(cell2 - cell1)
print(cell4 - cell3)

print('\nУмножаем')
print(cell2 * cell1)

print('\nДелим')
print(cell1 / cell2)

print('\nОрганизация ячеек по рядам')
print(cell1.make_order(5))
print(cell2.make_order(10))
