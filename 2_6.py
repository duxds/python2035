#Дана строка. Посчитайте количество "*", встречающихся в строке.
s = input('Введите строку')
c = 0
for i in s:
    if i =='*':
        c+=1
print(c)
