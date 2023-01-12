"""
Тестовые модули
---
Базовое задание:
Написать тесты для ДЗ уроков 1-8
1) не менее 10 тестов
2) желательно с разными функциями (assertEqual, assertRaises и т.д.)
3) тесты не должны быть вместе с исходным кодом (нужно разместить в разных модулях)

Задание НУЖНО!!!! сдать архивом

"""
import unittest
from seminar_09_scripts import my_func, diff_two_numb, int_func, duplicates_in_list, \
    DivisionByZero, division_by_zero_1, division_by_zero_2, int_gen, Cell, Road


class TestFunctions(unittest.TestCase):
    """
    Тесты
    """

    # ------------------------------------------------------------------------------(1)
    # Семинар: 3 / Базовое задание: 3
    def test_my_func_1(self):
        """
        Тест Equal
        """
        self.assertEqual(my_func(2, 4, 6), 10)

    def test_my_func_2(self):
        """
        Тест NotEqual
        """
        self.assertNotEqual(my_func(2, 4, 6), 6)

    # ------------------------------------------------------------------------------(2)
    # Семинар: 3 / Дополнительное задание: 3
    def test_diff_two_numb_1(self):
        """
        Тест Equal
        Тест проверки
        """
        self.assertEqual(diff_two_numb([1.1, 1.2, 3.1, 5, 10.01]), 0.19)

    def test_diff_two_numb_2(self):
        """
        Тест NotEqual
        """
        self.assertNotEqual(diff_two_numb([1.1, 1.2, 3.1, 5, 10.01]), 0.29)

    # ------------------------------------------------------------------------------(3)
    # Семинар: 3 / Базовое задание: 6
    def test_int_func(self):
        """
        Тест Equal
        """
        self.assertEqual(int_func('заглавная буква'), 'Заглавная Буква')

    # ------------------------------------------------------------------------------(4)
    # Семинар: 4 / Базовое задание: 4
    def test_duplicates_in_list(self):
        """
        Тест Equal
        """
        self.assertEqual(duplicates_in_list([2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]),
                         [23, 1, 3, 10, 4, 11])

    # ------------------------------------------------------------------------------(5)
    # Семинар: 8 / Базовое задание: 3
    def test_division_by_zero_1(self):
        """
        Тест Exception
        """
        self.failureException(division_by_zero_1(5, 0), 'Деление на ноль невозможно!')

    def test_division_by_zero_2(self):
        """
        Тест Raises
        """
        self.assertRaises(DivisionByZero, division_by_zero_2, 5, 0)

    # ------------------------------------------------------------------------------(6)
    # Семинар: 4 / Базовое задание: 6
    def test_int_gen_1(self):
        """
        Тест In
        """
        self.assertIn(4, int_gen(2, 7))

    def test_int_gen_2(self):
        """
        Тест NotIn
        """
        self.assertNotIn(8, int_gen(2, 7))

    # ------------------------------------------------------------------------------(7)
    # Семинар: 8 / Базовое задание: 2
    def test_class_objects_1(self):
        """
        Тест IsNot
        """
        self.assertIsNot(Cell(2), Cell(2))

    def test_class_objects_2(self):
        """
        Тест GreaterEqual
        """
        self.assertGreaterEqual(Cell(2).quantity, Cell(2).quantity)

    def test_class_objects_3(self):
        """
        Тест IsInstance
        """
        self.assertIsInstance(Cell(9), Cell)

    # ------------------------------------------------------------------------------(8)
    # Семинар: 7 / Базовое задание: 2
    def test_class_objects_4(self):
        """
        Тест IsNot
        """
        self.assertIsNot(Road(10, 20), Road(10, 20))


if __name__ == '__main__':
    unittest.main()
