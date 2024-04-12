def get_calc(a1, b1, c1):
    return int(a1) + int(b1) * int(c1)

v = input(f"Введите 3 числа через пробел: ").split(" ")
print(get_calc(v[0],v[1],v[2]))