"""
---
Дополнительное задание:
5. Реализуйте алгоритм перемешивания списка.
"""

import random as rnd


def list_mixer(list_in):
    lst = list_in[:]
    for i in range(len(lst)):
        i_rnd = rnd.randint(0, len(lst) - 1)
        temp = lst[i]
        lst[i] = lst[i_rnd]
        lst[i_rnd] = temp
    return lst


initial_list = []
for j in range(0, 10):
    initial_list.append(j)
final_list = list_mixer(initial_list)

print(f"{initial_list}  ->  {final_list}")
