with open('1.txt', 'w+') as file:
    file.write((input("Введите 10 чисел: ")))

with open('1.txt', 'r') as file:
    s = list(map(int, file.read().split()))

maximum = max(s)
minimum = min(s)

with open('2.txt', 'w+') as file:
    file.write(str(maximum) + " " + str(minimum))

with open('2.txt', 'r') as file:
    print(file.read())




