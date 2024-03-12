#Создайте двумерный список размерностью 4x3, заполненный случайными значениями в диапазоне от 1 до 100.
#Посчитайте количество элементов, значение которых меньше 10ти.
import random
ls = [[random.randint(1, 100) for j in range(3)] for i in range(4)]
sum = 0
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] < 10:
            sum += ls[i][j]
print(sum)
print(ls)
