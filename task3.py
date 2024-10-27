# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3
import random

opr=0

N=int(input())
mas=[random.randint(0,100) for i in range(N)]
#print(mas)
for i in range(100):
    string=""
    for j in range(N):
        if mas[j]==i:
            string+=str(j)+' и '
    if string!='' and len(string.split())>2:
        print("значение"+str(i)+":"+string[0:len(string)-3])
        opr+=1
if opr==0:
    print("Нет")
