import math
def get_points(ar):
    for i in range(3):
        x = int(input(f"x{i+1}: "))
        y = int(input(f"y{i+1}: "))
        ar.append((x,y))

def get_segments(x1, x2, y1, y2):
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

def get_perim(array, n=3):
    if n == 1:
        return get_segments(array[0][0], array[-1][0], array[0][1], array[-1][1])
    else:
        return get_segments(array[n-1][0], array[n-2][0], array[n-1][1], array[n-2][1]) + get_perim(array, n-1)

arr = []
get_points(arr)
print(f"Периметр треугольника: {round(get_perim(arr), 2)}")




