import numpy as np

def profile(n: int, m: int):
    if n % 2 == 1 or m % 2 == 1:
        return None
    L = pow(2, n - 1)
    can = np.zeros((L, L), dtype=int)
    arr = np.zeros((m + 1, L), dtype=int)
    for i in range(m):
        for j in range(L):
            for c in range(L):
                if can[j][c] == 1:
                    arr[i + 1, c] += arr[i, j]
    return arr[0, m]

if __name__ == '__main__':
    print(profile(2, 2))

"""

n*m

m * 2^n-1

    m   m+1
    ...
..
2   ?   +Q  
..
24  ?   +Q
..
37  Q
..


"""
