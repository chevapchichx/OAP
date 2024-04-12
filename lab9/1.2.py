with open('1_2.txt', 'w') as file:
    N = int(input("Количество чисел: "))
    for i in range(N):
        nums = float(input(f"{i+1} число: "))
        file.write(str(nums) + ' ')

with open('1_2.txt', 'r') as file:
    print(file.read())

