h1 = int(input())
h2 = int(input())
h3 = int(input())
h4 = int(input())
h5 = int(input())

visible_buildings = "1"

if h2 > h1:
    visible_buildings += " 2"
if h3 > max(h1, h2):
    visible_buildings += " 3"
if h4 > max(h1, h2, h3):
    visible_buildings += " 4"
if h5 > max(h1, h2, h3, h4):
    visible_buildings += " 5"

print(visible_buildings)








