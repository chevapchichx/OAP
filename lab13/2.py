# t = 25
# def wop():
#     print("Внешняя функция wop")
#     def get_pow(a):
#         b = pow(a,2)
#         print(f"25 в степени 2: {b}")
#     get_pow(t)
# wop()

# def out_func():
#     w = 2
#     q = 4
#     print(f"w = {w}, q = {q}")
#     def in_func():
#         id_w = id(w)
#         id_q = id(q)
#         print(f"ID w: {id_w}, ID q: {id_q}")
#     in_func()
# out_func()

# def out_func():
#     def in_func():
#         print("Вложенная функция in_func")
#     return in_func()
#
# out_func()