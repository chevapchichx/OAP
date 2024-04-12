# def check_numbers(a):
#     if not a.isdigit():
#         print(f"'{a}' не является целым положительным числом. Попробуйте еще раз")
#         return False
#     if len(a) != 3:
#         print(f"Длина введенного числа: {len(a)}. Попробуйте еще раз")
#         return False
#     return True
#
# def get_sum(num_str):
#     result = 0
#     for i in range(len(num_str)):
#         result += int(num_str[i])
#     return result
#
# max_num = ""
# max_sum = 0
# for i in range(3):
#     while True:
#         num = input(f"Введите трехзначное целое положительное число {i + 1}: ")
#         if check_numbers(num):
#             break
#     val = get_sum(num)
#     if val > max_sum:
#         max_sum = val
#         max_num = num
#
# print(f"Максимальная сумма цифр: {max_sum} (число: {max_num})")

def xui():
    print(6)

xui()