arr = []
with open('9_4_in.txt', 'r') as file:
    for i in file:
        val = i.split(" ")
        arr.append((int(val[2]), i))

a = sorted(arr)

with open('9_4_out.txt', 'w') as file:
    i = 0
    min_age = a[i][0]
    age = min_age
    while age <= min_age:
        if i < len(a)-1:
            age = a[i+1][0]
        else:
            age += 1
        file.write(f"{a[i][1]}\n")
        i += 1

    i = len(a)-1
    max_age = a[i][0]
    age = max_age
    while age >= max_age:
        if i > 0:
            age = a[i-1][0]
        else:
            age = 0
        file.write(f"{a[i][1]}\n")
        i -= 1

