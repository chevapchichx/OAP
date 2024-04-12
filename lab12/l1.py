def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_thre( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_two(3, 6))
