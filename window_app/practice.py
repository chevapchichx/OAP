class Practice:
    x = 50      # атрибут класса (свойство класса)


c1, c2 = Practice(), Practice()   # экземпляры (объекты)

c1.y = 10       # атрибут экземпляра (свойство объекта) класса c1
c2.y = 20       # атрибут экземпляра (свойство объекта) класса c2

Practice.x = 60

print(f'{c1.x}, {c1.y}')
print(f'{c2.x}, {c2.y}')



