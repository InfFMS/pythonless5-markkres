# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
import random
N=int(input())
uni=[]
mas=[random.randint(0,100) for i in range(N)]
print(mas)
for i in range (N):
    a=0
    for j in range(len(uni)):
        if uni[j]==mas[i]:
            a=1
            break
    if a==0:
        uni.append(mas[i])
print(uni)
