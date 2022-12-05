"""
---
Базовое задание:
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""


def monthCheck():
    monthBool = True
    while monthBool:
        month = input('Введите номер месяца: ')
        try:
            month = int(month)
            if month < 1 or month > 12:
                print('Ошибка ввода! Повторите попытку.')
            else:
                while monthBool:
                    var = input('Введите вариант решения задачи [1 - list] / [2 - dict]: ')
                    try:
                        var = int(var)
                        if var == 1:
                            seasonInt = (month % 12) // 3
                            print(f'Сезон указанного месяца: {seasonsList[seasonInt]}')
                            monthBool = False
                        elif var == 2:
                            month = str(month)
                            for i in seasonsDict:
                                if month in seasonsDict.get(i):
                                    print(f'Сезон указанного месяца: {i}')
                                    monthBool = False
                    except ValueError:
                        print("Ошибка ввода! Введите значение 1 или 2.")
        except ValueError:
            print("Ошибка ввода! Введите значение от 1 до 12.")


seasonsList = ['Зима', 'Весна', 'Лето', 'Осень']

seasonsDict = {'Зима': ('1', '2', '12'),
               "Весна": ('3', '4', '5'),
               "Лето": ('6', '7', '8'),
               "Осень": ('9', '10', '11')}
monthCheck()
