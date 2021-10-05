import math

s = "Ф"

genMap = " ФABCDEFGHJIKLMNOPQ 321RSTUVWXYZ"
map = dict()

i = 1
for a in genMap:
    if a.isalpha():
        map[a] = i
        i += 1

r = 0
for a in s:
    if a.isalpha():
        r += map.get(a, 0)
print(r)
