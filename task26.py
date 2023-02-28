# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def stepen(a,b):
#     if b == 1:
#         return (stepen)
#     if b != 1:
#         return(a*stepen(a,b-1))

# print(stepen(2,3))

def rec(a, b):
    if (b == 0):
        return 1
    elif (b == 1):
        return (a)
    else:
        return (a * rec(a, b - 1))
a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", rec(a, b))