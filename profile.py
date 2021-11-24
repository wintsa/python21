import numpy as np


def bit(n: int, p: int):
    p = 1 << p
    return (n & p) >> p


def fill(profile, pos, len):

    return []


def profile(n: int, m: int):
    if n % 2 == 1 or m % 2 == 1:
        return None
    L = 1 << n
    can = np.zeros((L, L), dtype=int)
    for i in range(L):
        can[i] = fill(i, 0, 0)
    arr = np.zeros((m + 1, L), dtype=int)
    for i in range(m):
        for c in range(L):
            for j in range(L):
                arr[i + 1, c] += arr[i, j] * can[j, c]
    return arr[m + 1, 0]


if __name__ == '__main__':
    print(profile(2, 2))



"""

n*m

m * 2^n

    m   m+1
    ...
..
2   ?   +Q  
..
26  ?   +Q
..
37  Q
..


"""
