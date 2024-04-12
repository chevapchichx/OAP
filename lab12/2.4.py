def get_multi(numbers):
    c = 1
    for i in numbers:
        c *= i
    return c

v = [1, 2, 3, 0, 5]
print(f"Произведение чисел {v} = {get_multi(v)}")