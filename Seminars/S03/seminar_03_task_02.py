"""
---
Базовое задание:
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def name_surname(name, surname):
    """
    Функция объединяет имя и фамилию.
    """
    return name + ' ' + surname


def user_data_inline(full_name, year, city, email, tel):
    """
    Функция выводит одной строкой входящие данные.
    full_name, year, city, email, tel - Входящие данные.
    """
    print(f'{full_name} {year} {city} {email} {tel}')


# input_name = input('Введите имя: ')
# input_surname = input('Введите фамилию: ')
# input_year = input('Введите год рождения: ')
# input_city = input('Введите город проживания: ')
# input_email = input('Введите адрес электронной почты: ')
# input_tel = input('Введите номер телефона: ')
input_name: str = 'Владимир'
input_surname: str = 'Иванов'
input_year: str = '1985'
input_city: str = 'Омск'
input_email: str = 'vladimirivanov1985@mail.ru'
input_tel: str = '8-999-300-20-10'

user_data_inline(full_name=name_surname(name=input_name, surname=input_surname),
                 year=input_year,
                 city=input_city,
                 email=input_email,
                 tel=input_tel)
