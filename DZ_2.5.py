# 5. Реализуйте алгоритм перемешивания списка.

from random import shuffle

a = input("Введите числа: ").split(",")
print(f'Не перемешанный список - > {a}')
shuffle(a)
print(f'Перемешанный список - > {a}')
