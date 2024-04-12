def dec2(n):
    h, m = "", ""
    while n != 0:
        if n%16 == 15:
            h = "F"
        elif n%16 == 14:
            h = "E"
        elif n%16 == 13:
            h = "D"
        elif n%16 == 12:
            h = "C"
        elif n%16 == 11:
            h = "B"
        elif n%16 == 10:
            h = "A"
        else:
            h = str (n%16)
        m = h + m
        n //= 16
        return "{0:0>4}".format(m)

a = int(input())
print(dec2(a))
