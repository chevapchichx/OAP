import random

with open('f.txt', 'w') as f:
    N = int(input("Количество чисел: "))
    for i in range(N):
        nums = random.randint(1, 1000)
        f.write(str(nums) + '\n')

with open('f.txt', 'r') as f:
    print(f.read())

with open('f.txt', 'r') as f1, open('g.txt', 'w') as g:
    for i in f1:
        i = int(i)
        if i % 2 == 0:
            g.write(str(i) + ' ')

with open('g.txt', 'r') as g:
    print(g.read())