def recursive(i):
    print(i, end=" ")
    if i < 4:
        recursive(i + 1)
    print(i, end=" ")

recursive(1)
