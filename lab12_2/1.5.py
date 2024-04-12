def isPrime(N):
    res = 1
    for i in range(2, N):
        if N%i == 0:
            break
        else:
            res = 0
    return res

a = int(input())
out = 0
while a > 0:
    if a == 1:
        out += 1
    break

out += isPrime(a)
a //= 10
if out == 0:
    print("YES")
else:
    print("NO")
