with open('input.txt', 'w+') as f_input:
    f_input.write((input("Введите 10 чисел: ")))

with open('input.txt', 'r') as f_input:
    s = list(map(int, f_input.read().split()))

f = 1
for i in s:
    f *= i

with open('output.txt', 'w+') as f_output:
    f_output.write(str(f))
    print(f)
