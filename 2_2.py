d = input('Введите строку слов с пробелами ')
s = 'ауеыоиэяюёЁАУИЕЫОЭЯЮ'
d = d.split(' ')
allsum = 0
for i in d:
    sum = 0
    for j in i:
        if j in s:
            sum+=1
    print(f'Гласных в слове  {i} - {sum}')
    allsum +=sum
print(allsum)

