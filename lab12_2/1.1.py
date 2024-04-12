# def get_num(a):
#     a = str(a)
#     for i in range(len(a)):
#         print(a[i])
#
# n = abs(int(input()))
# get_num(n)

def deviders(n):
    res, r1, r2 = "","",""
    d1, d2 = 1, n
    while d1 != d2:
        if n % d1 == 0:
            d2 = n//d1
        r1 = r1 + str(d1) + " "
        r2 = str(d2) + " " + r2
        d1 += 1
        res = res + r1 + r2
        return res.strip()

print(deviders(90))
