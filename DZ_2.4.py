# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение 
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

a = int(input("Введите число: "))
sum = 0
num = []
for i in range(-a,a + 1):
    num.append(i)
    i += 1
print(num)

file = "file.txt"
data = open(file, 'r')
product = 1
for h in data:
    product *= num[int(h)]
print(f'Произведение чисел = {product}')

