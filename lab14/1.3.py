def fibonachi(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonachi(n-1) + fibonachi(n-2)


num = int(input("Введите число: "))
print(f"fibonachi = {fibonachi(num)}")
for i in range(num):
    print(fibonachi(i))