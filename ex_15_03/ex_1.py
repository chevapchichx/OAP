import math
def check_numbers(a):
    while a.replace(".","").isdigit():
        return True
    else:
        print(f"'{a}' не может быть радиусом. Попробуйте еще раз")
        return False

while True:
    radius1 = input("Введите значение внутреннего радиуса кольца: ")
    if check_numbers(radius1):
        break
while True:
    radius2 = input("Введите значение внешнего радиуса кольца: ")
    if check_numbers(radius2):
        break

r1 = float(radius1)
r2 = float(radius2)
if r1 >= r2:
    print("Внутренний радиус не может превышать внешний. Попробуйте еще раз")
else:
    circle = round(math.pi * (r2**2 - r1**2),2)
    print(f"Площадь кольца: {circle}")
