# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
import random
import math
N=int(input())
a=[random.randint(-1000,1000) for i in range(N)]
b=[random.randint(-1000,1000) for i in range(N)]
print("вектор a =",a)
print("вектор b =",b)
dlinA,dlinB,scal=0,0,0
for i in range(N):
    dlinA+=a[i]**2
    dlinB+=b[i]**2
    scal+=a[i]*b[i]
dlinA=dlinA**0.5
dlinB=dlinB**0.5
print(math.acos(scal/(dlinA*dlinB)))
