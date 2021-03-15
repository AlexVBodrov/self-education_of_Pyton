"""
День 4: Проблемы программирования средней сложности (6 часов): перевернуть строку (проверить на палиндром),
посчитать наибольший общий делитель,
объединить два отсортированных массива,
написать игру на угадывание чисел,
посчитать возраст и т.д.
"""

#перевернуть строку (проверить на палиндром)

a ="qwerty"
b ="abba"
aa = a[::-1]
print(aa)
print(b[::-1] )
if b == b[::-1]:
    print(f'{b} это - палиндром')
    

#посчитать наибольший общий делитель

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)

gcd(int(input("a : ")), int(input("b : ")))

"""
написать игру на угадывание чисел,

"""

while True:
    user_number = int(input("Угадайте число от 1 до 100 : "))
    if user_number == ask_number:
        print("Вы угадали")
        break
    elif user_number < ask_number:
        print("Загадное число больше вашего")
    else:
        print("Загадное число меньше вашего")

# объединить два отсортированных массива

arr1 = [1, 1, 3,4,5,3]
arr2 = [2,4,6,8]
print(sorted(arr1 + arr2))

# посчитать возраст и т.д
from datetime import datetime
current_year = datetime.now().year
print(current_year - int(input("Введите год рождения : ")))
