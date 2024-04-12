def deviders(n):
    res, r1, r2 = "","",""
    d1, d2 = 1, n
    while d1 != d2:
        if n%d1 == 0:
            d2 = n//d1
            r1 = r1 + str(d1) + " "
            r2 = str(d2) + " " + r2
        d1 += 1
    res = res + r1 + r2
    return res.strip()

n = int(input())
n = abs(n)
print(deviders(n))