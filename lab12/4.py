def get_reverse(stri):
    rev_stri = ""
    l = len(stri)
    while l > 0:
        rev_stri += stri[l - 1]
        l -= 1
    return rev_stri

c = "1234abcd"
print(get_reverse(c))
