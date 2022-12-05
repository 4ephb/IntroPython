"""
---
Базовое задание:
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
feature = "название", "цена", "количество", "ед"
products, names, prices, quantities, units = [], [], [], [], []
analytics = {feature[0]: names, feature[1]: prices, feature[2]: quantities, feature[3]: units}


def int_input_check():
    num = ''
    loop = True
    while loop:
        num = input('Количество добавляемых товаров: ')
        try:
            num = int(num)
            loop = False
        except ValueError:
            print("Ошибка ввода! Введите числовое значение.")
    return num


def products_add(num):
    for i in range(num):
        print(f"\n{i + 1}-й товар:")
        prod_add = dict({feature[0]: input("\tНазвание : "),
                         feature[1]: input("\tЦена : "),
                         feature[2]: input('\tКоличество : '),
                         feature[3]: input("\tЕдиница измерения : ")})
        products.append((i + 1, prod_add))
        names.append(products[i][1].get(feature[0]))
        prices.append(products[i][1].get(feature[1]))
        quantities.append(products[i][1].get(feature[2]))
        units.append(products[i][1].get(feature[3]))


def products_print(num):
    print(f"\nСтруктура товаров:")
    for i in range(num):
        print(f'\t{products[i]}')
    print(f"\nАналитика:\n\t{analytics}")


amount = int_input_check()
products_add(amount)
products_print(amount)
