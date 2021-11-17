import numpy as np

map = np.array([[2, 3, 5, 3],
                [1, 2, 3, 4],
                [3, 7, 1, 1]])

a = np.ones((6,2), dtype=int)
b = np.zeros_like(map)
d = np.ones_like(map)
c = map*2 + 1

e = a.reshape((3,4)) + c

print(map, a, b, c, e, sep='\n')

print(np.cumprod(map).reshape(map.shape))

print(map.shape)

