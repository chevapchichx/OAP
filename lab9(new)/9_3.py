def sum_of_digits(n):
    c = 0
    while n > 0:
        digit = n % 10
        c = c + digit
        n //= 10
    return c

with open('9_3_in.txt', 'w+') as file:
    file.write((input("Введите 10 чисел: ").replace(" ", "\n")))

s = []
with open('9_3_in.txt', 'r') as file:
    for i in file:
        val = int(i.strip())
        s.append((sum_of_digits(val), val))

a = sorted(s)

with open('9_3_out.txt', 'w+') as file:
     for i in a:
        file.write(f"{str(i[1])}\n")

with open('9_3_out.txt', 'r') as file:
    print(file.read())