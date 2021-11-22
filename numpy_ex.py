import numpy as np



python2d = [[2, 3, 5, 3],
            [1, 2, 3, 4],
            [3, 7, 1, 1]]
map = np.array(python2d)

print(python2d[1][1], map[1, 1])

print(map.dtype)

a = np.ones((6, 2), dtype=int)
b = np.zeros_like(map)
d = np.ones_like(map)
c = map * 2 + 1

e = a.reshape((3, 4)) + c

print(map, a, b, c, e, sep='\n')

print(np.cumprod(map).reshape(map.shape))

print(map.shape)

np.info(np.ndarray.dtype)

comp = a.reshape(map.shape) == map

h = np.random.random((3, 3, 3))

print(h)

t = [[0, 1], [0, 0], [0, 0]]

print(h[t])
print(h[h > 0.5])
