num_arr = []
with open('2_6.txt', 'w+') as file:
    N = int(input("Количество чисел: "))
    for i in range(N):
        nums = float(input(f"{i + 1} число: "))
        file.write(str(nums) + ' ')
        num_arr.append(nums)
diff = num_arr[0] - num_arr[-1]
print(diff)

