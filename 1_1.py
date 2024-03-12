#Разработайте приложение на языке Python для решения задачи «Генератор безопасных паролей». 
#Необходимо разработать и представить программу, которая генерирует пароли для пользователя десктопных, мобильных и веб-приложений.
import random
n=int(input('Задайте длину пароля '))
simvolpress='1234567890!@#$%^&*()_+="№;:?[]{}\|/,.<>qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
mypassword = ''
for i in range(n):
    mypassword += random.choice(simvolpress)
print(mypassword) 
