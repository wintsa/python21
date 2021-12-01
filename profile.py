"""
Задача про домино
Сколькими способами можно замостить доску n*m костями домино?
n и m — четные
"""
import numpy as np

def bit(n: int, p: int):
    p2 = 1 << p
    return (n & p2) >> p

def fill(can, p, n, profile, len):
    if len == n:
        can[p][profile] = 1
        return
    if bit(p, len) == 0:
        fill(can, p, n, profile + (1 << len), len + 1)
        if len < n - 1 and bit(p, len + 1) == 0:
            fill(can, p, n, profile, len + 2)
    else: # == 1
        fill(can, p, n, profile, len + 1)
    return

def profile(n: int, m: int):
    if n % 2 == 1 or m % 2 == 1:
        return None
    L = 1 << n
    can = np.zeros((L, L), dtype=int)
    for i in range(L):
        fill(can, i, n, 0, 0)
#    print(can[37])
#    for i in range(L):
#        if can[37][i] == 1:
#            print(f"{i:0{n}b}", i)
    arr = np.zeros((m + 1, L), dtype=int)
    arr[0, 0] = 1
    for i in range(m):
        for c in range(L):
            for j in range(L):
                arr[i + 1, c] += arr[i, j] * can[j, c]
    print(arr.T)
    return arr[m, 0]

if __name__ == '__main__':
    print(profile(2, 4))

"""


[[1 1 2 3 5]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 1 1 2 3]]


n*m

0 1 
0 1
0 0

m * 2^n

    m   m+1
    ...
..
2   ?   +Q*1  
..
26  ?   +Q*1
..
37  Q   +Q*0
..


"""
