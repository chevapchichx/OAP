def get_multi(num):
    c = 1
    for i in num:
        c *= i
    return c

numbers = [8, 2, 3, -1, 7]
print(get_multi(numbers))