def Y (a, b, c):
    d = b**2-4*a*c
    if d > 0:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print('Корни уравнения ', x1, x2)

    elif d == 0:
        x1 = x2 = (-b + d**0.5)/(2*a)
        print('Два одинаковых корня ', x1, x2)
    else:
        print('Корней нет ')
        
