# m = int(input("Введите число 1: "))
# n = int(input("Введите число 2: "))
#
# while m != n:
#     if m > n:
#         m -= n
#     else:
#         n -= m
#
# print(f"НОД чисел: {m}")


num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))

def get_nod(m, n):
    if m != 0:
        return get_nod(n % m, m)
    else:
        return n

print(f"НОД чисел: {get_nod(num1, num2)}")