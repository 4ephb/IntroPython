"""
---
Базовое задание:
2. Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с
индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

print('Заполните список. Для завершения заполнения списка нажмите Enter.\n')
input_list = []
i = 1
while True:
    list_element = input(f'{i}-й элемент: ')
    if list_element == '':
        print(f'Ввод значений элементов списка завершен.')
        break
    if list_element is not None:
        input_list.append(list_element)
    i += 1
print(input_list)

list_final_len = len(input_list)
if list_final_len % 2 != 0:
    list_final_len -= 1
for i in range(0, list_final_len, 2):
    input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
print(input_list)
