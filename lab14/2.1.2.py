def get_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + get_sum(n // 10)

def get_max_sum(number):
    max_sum = 0
    max_num = 0
    val = get_sum(number)
    if val > max_sum:
        max_sum = val
        max_num = number
    print(f"Максимальная сумма цифр: {max_sum} (число: {max_num})")

num = 0
for i in range(3):
    num = int(input(f"Введите целое число {i + 1}: "))
get_max_sum(num)