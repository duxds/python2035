
a = [3, -14, 5, -6, 7]
#список сортируем модулем
a = sorted(a, key=abs, reverse=True )
print(a)


s=['яблоко', 'груша', 'слива']
#самое большое значение длины
naib = 0
for i in s:
    if len(i)>naib:
        naib=len(i)
for i in range(len(s)):
    if len(s[i])<naib:
       s[i]+='_'*(naib-len(s[i]))
print(s)
