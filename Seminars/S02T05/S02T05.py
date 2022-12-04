"""
---
Базовое задание:
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""


def intInputCheck(lst):
    while True:
        num = input('Введите новый элемент рейтинга: ')
        if str(num) == '':
            break
        else:
            Loop = True
        try:
            num = int(num)
            while Loop:
                lst.append(num)
                lst.sort(reverse=True)
                print(f'Результат: {lst}')
                Loop = False
        except ValueError:
            print("Ошибка ввода! Введите числовое значение.\n"
                  "Для завершения ввода нажмите клавишу Enter. ")


my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг: {my_list}")
intInputCheck(my_list)