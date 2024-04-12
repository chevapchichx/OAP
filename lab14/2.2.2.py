def get_nod(m, n):
    if m == 0:
        return n
    else:
        r = n % m
        return get_nod(r, m)

num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))

print(f"НОД чисел: {get_nod(num1, num2)}")