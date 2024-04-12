with open('1_3.txt', 'w') as file:
    N = int(input("Количество чисел: "))
    for i in range(N):
        nums = int(input(f"{i+1} натуральное число: "))
        if nums <= 0:
            print("Число не натуральное. Попробуйте заново")
            break
        else:
            file.write(str(nums) + ' ')

with open('1_3.txt', 'r') as file:
    print(file.read())


