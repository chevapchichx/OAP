r = {"Tom", "Sem", "Alex", "Bob", "Alice", "Tom"}
print(f"Множество r: {r}")
t = {"Sem", "AliceR", "Tom"}
print(f"Множество t: {t}")

f = len(t)
print(f"Длина множества t: {f}")
r.discard("Tom")
print(f"Множество r без первого элемента: {r}")
u = r.union(t)
print(f"Объединение множеств r и t: {u}")
d = r.intersection(t)
print(f"Пересечение множеств r и t: {d}")
e = r.difference(t)
print(f"Разность элементов t из элементов r: {e}")
y = t.copy()
print(f"Копия множества t: {y}")