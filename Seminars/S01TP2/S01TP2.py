"""
Семинар 01
---
Дополнительное задание:
2. Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

state_left = False
state_right = False

for x in range(2):
    for y in range(2):
        for z in range(2):
            state_left = not (bool(x) or bool(y) or bool(z))
            state_right = not bool(x) and not bool(y) and not bool(z)
            print(f'При значении X = {bool(x)}, Y = {bool(y)}, Z = {bool(z)}, '
                  f'утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является {state_left == state_right}')
