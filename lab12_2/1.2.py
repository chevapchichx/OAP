def get_divide(a):
    c = 0
    v = a
    while c != a:
        c += 1
        if a % c == 0:
            v = a // c
            print(f"{v}", end=' + ')

n = int(input("Введите число: "))
get_divide(n)



