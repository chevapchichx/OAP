def get_fact(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * get_fact(n-1)

v = int(input("Введите число: "))
print(f"{v}! = {get_fact(v)}")