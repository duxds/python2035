#1. Реализуйте проверку введённого пароля таким образом, чтобы проверка шла до тех пор, пока не введут верный пароль.
#2. Создайте программу для определения квадрата числа в последовательности от n до m.
#1
password = input('Введите пароль ')
password2 = input('Введите пароль ещё раз ')
while password2 != password:
    password2 = input('Введите пароль ещё раз ')
print('Пароль правильный')
#2
n = int(input('Введите натуральное число '))
m = int(input('Введите натуральное число '))
for i in range(n, m+1):
    print(i**2, end = ' ')

