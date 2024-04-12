def get_min(numbers):
    c = numbers[0]
    for i in numbers:
        if i < c:
            c = i
    return c

v = input("Введите 3 числа через пробел: ").split(" ")
print(f"Минимальное число: {get_min(v)}")
