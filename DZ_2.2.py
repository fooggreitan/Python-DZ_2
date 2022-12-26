# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math
a = int(input("Введите число: "))
liat_a = []
if a == 0: print(1)
else:
    for i in range(a):
        i += 1
        liat_a.append(math.factorial(i))
print(liat_a)
        