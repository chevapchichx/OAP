A = {"Alina", "Boris", "Dima", "Elena", "Sveta", "Masha", "Vanya", "Katya", "Nina"}
B = {"Alina", "Dima", "Elena", "Sveta", "Katya"}
C = {"Boris", "Masha", "Vanya", "Nina"}
D = {"Alina", "Sveta", "Vanya", "Nina"}
E = {"Alina", "Vanya", "Dima", "Boris"}

BD = B.intersection(D)
print(f"Отличники, учащиеся в старших классах: {BD}")
CD = C.intersection(D)
print(f"Отличники, учащиеся в младших классах: {CD}")
BE = B.intersection(E)
print(f"Спортсмены, учащиеся в старших классах: {BE}")
CE = C.intersection(E)
print(f"Спортсмены, учащиеся в младших классах: {CE}")
BDE = BD.intersection(BE)
print(f"И спортсмены, и отличники учащиеся в старших классах: {BDE} ")
CDE = CD.intersection(CE)
print(f"И спортсмены, и отличники учащиеся в младших классах: {CDE} ")
B_diff = B.difference(BD.union(BE))
print(f"Ни спортсмены, ни отличники учащиеся в старших классах: {B_diff}")
C_diff = C.difference(CD.union(CE))
print(f"Ни спортсмены, ни отличники учащиеся в младших классах: {C_diff}")
