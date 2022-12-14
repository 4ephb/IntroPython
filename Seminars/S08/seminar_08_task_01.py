"""
---
Базовое задание:
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    """Базовый класс Matrix."""
    result_list = []

    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        return str('\n'.join('\t'.join([str(el) for el in i]) for i in self.m_list))

    def __add__(self, other):
        count = 0
        try:
            # проверяем соответствие размеров матриц
            if len(self.m_list) == len(other.m_list):
                for i in range(int(len(self.m_list))):
                    if len(self.m_list[i]) == len(other.m_list[i]):
                        count += 1
                if count == len(other.m_list):
                    self.result_list = [[0] * len(self.m_list[0]) for _ in range(len(self.m_list))]
            # производим вычисление и заполняем новую матрицу
            for i in range(int(len(self.m_list))):
                for j in range(int(len(other.m_list[i]))):
                    self.result_list[i][j] = self.m_list[i][j] + other.m_list[i][j]
        except IndexError:
            print('Размеры матриц различаются!\n'
                  'Задайте матрицы одинакового размера.\n')
        return Matrix(self.result_list)


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

m_1 = Matrix(matrix_1)
print('Матрица 1:')
print(f'{m_1}\n')

m_2 = Matrix(matrix_2)
print('Матрица 2:')
print(f'{m_2}\n')

print(f'Сумма матриц:\n{m_1 + m_2}')
