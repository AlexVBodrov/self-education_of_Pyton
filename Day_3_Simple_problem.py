"""
День 3: Простые проблемы программирования (5 часов):
поменять местами две переменные,
перевести градусы Цельсия в градусы по Фаренгейту,
посчитать сумму всех разрядов в числе, проверить число на простоту,
сгенерировать случайное число, удалить дубликат из списка
"""
#1 поменять местами две переменные,
a = 2
b = 3
print(f' a = > {a}')
print(f' b = > {b}')
print("Magika")
a,b = b,a
print(f' a = > {a}')
print(f' b = > {b}')

# перевести градусы Цельсия в градусы по Фаренгейту, Convert Celsius to Fahrenheit
celsius = float(input('Input °C Celsius : '))
celsius_to_Fahrenheit = (celsius * (9/5)) + 32
print(f'Convert  {celsius} °C Celsius to Fahrenheit => {celsius_to_Fahrenheit :.2f} °F')


#посчитать сумму всех разрядов в числе
print('Количество разрядов:', len(str(abs(int(input('Введите число,чтобы посчитать сумму всех разрядов в числе: '))))))


# проверить число на простоту
from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True

num = int(input('Введите число,чтобы  проверить число на простоту: '))
print(is_prime(num))


#  сгенерировать случайное число
import random
print(f'Рандомное число от 1 до 100 => {random.randint(1,100)}\n')

#удалить дубликат из списка
def del_dups(mylist):
    # удалить дубликат из списка
    # сравнить индекс с остальными
    # удалить копии- ошибочно/// просто не добавлять в новый список
    # создать новый список и вернуть
    newlist = []
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    return newlist

my_list = [8, 8, 9, 9, 7, 15, 15, 2, 20, 13, 2, 24, 6, 11, 7, 12, 4, 10, 18,
       13, 23, 11, 3, 11, 12, 10, 4, 5, 4, 22, 6, 3, 19, 14, 21, 11, 1,
       5, 14, 8, 0, 1, 16, 5, 10, 13, 17, 1, 16, 17, 12, 6, 10, 0, 3, 9,
       9, 3, 7, 7, 6, 6, 7, 5, 14, 18, 12, 19, 2, 8, 9, 0, 8, 4, 5]
print(f'удалить дубликат из списка : {my_list} \n\n result => {del_dups(my_list)}')
#print(del_dups(my_list))
# -> [8, 9, 7, 15, 2, 20, 13, 24, 6, 11, 12, 4, 10, 18, 23, 3, 5, 22, 19, 14,
#     21, 1, 0, 16, 17]


