import math

def get_circle(radius1, radius2):
    if radius1 >= radius2:
        return "Внутренний радиус не может превышать внешний. Попробуйте еще раз"
    else:
        circle = round(math.pi * (radius2**2 - radius1**2),2)
        return f"Площадь кольца: {circle}"

r1 = float(input("Введите значение внутреннего радиуса кольца: "))
r2 = float(input("Введите значение внешнего радиуса кольца: "))
print(get_circle(r1, r2))