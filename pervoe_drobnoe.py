# Напишите программу, которая будет принимать на вход дробь 
# показывать первую цифру дробной части числа.
# Примеры:

# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

numbers = float(input("Введите число: "))
b = numbers % 1 * 10
if b==0:
    print("Нет")
else:
    print(int(b))
