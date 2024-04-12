def get_fact(num):
    c = 1
    while num > 0:
        c *= num
        num -= 1
    return c

v = int(input("Введите число для расчета факториала: "))
print(get_fact(v))