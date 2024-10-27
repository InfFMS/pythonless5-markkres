# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
import random

b=0

n=int(input())
mas=[random.randint(0,1000) for i in range(n)]

#print(mas)

print(n)
print(mas[-1])
print(mas[::-1])
for i in range(n):
    if len(str(mas[i]))==3 and str(mas[i])[0]==str(mas[i])[1] and str(mas[i])[0]==str(mas[i])[2]:
        b=1
        break
if b==1:
    print("YES")
else:
    print("NO")
mas.pop(0)
mas.pop(-1)
print(mas)
