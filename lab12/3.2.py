def get_reverse(stri):
    return stri[:: -1]

c = "123 abc"
print(f"Перевернутая строка '{c}' = '{get_reverse(c)}'")