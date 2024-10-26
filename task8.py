# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
import random

def odin(num):
    string=str(num)
    a=0
    for i in range(1,len(string)):
        if string[i]!=string[i-1]:
            a=1
            break
    if a==1: return False 
    else: return True
N=int(input())
mas=[random.randint(10,10000) for i in range(N)]
print(mas)
otv=[]
for i in range(N):
    if odin(mas[i]):
        otv.append(mas[i])
print(otv)
