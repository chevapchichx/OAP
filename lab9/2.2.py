with open('f.txt', 'w') as f:
    N = int(input("Количество чисел: "))
    for i in range(N):
        nums = int(input(f"{i + 1} натуральное число: "))
        if nums <= 0:
            print("Число не натуральное. Попробуйте заново")
            break
        else:
            f.write(str(nums) + '\n')

K = int(input("K: "))
with open('f.txt', 'r') as f, open('2_2.txt', 'w') as file:
    for i in f:
        i = int(i)
        if i % K != 0:
            file.write(str(i) + '\n')

with open('2_2.txt', 'r') as file:
    f = file.readlines()
    print(f)
