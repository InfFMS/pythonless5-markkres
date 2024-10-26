# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
import random

N=int(input())
mas=[random.randint(0,1000) for i in range(N)]
print(mas)
udal=[]
sredn=sum(mas)/N
print(sredn)
for i in range(N):
    if mas[i]>=1.3*sredn or mas[i]<=0.7*sredn:
        print(mas[i])
        udal.append(i)
udal.sort(reverse=True)
for i in udal:
    mas.pop(i)
print(mas)
