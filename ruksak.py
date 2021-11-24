import numpy as np


def ruksak(weights: list, prices: list, W: int):
    """
    Решение целочисленной задачи рюкзака
    :param weights целочисленные веса предметов
    :param prices цены предметов
    :param W объем рюкзака
    """
    L = len(weights)
    if len(prices) != L:
        return None
    s = np.zeros((L + 1, W + 1), dtype=int)
    for i in range(L):
        w = weights[i]
        p = prices[i]
        for j in range(W):
            s[i + 1, j + 1] = max(s[i, j + 1], s[i + 1, j])
            if j + 1 >= w:
                new_price = s[i, j + 1 - w] + p
                if new_price > s[i + 1, j + 1]:
                    s[i + 1, j + 1] = new_price
    print(s)
    i = L
    j = W
    ret = []
    while i > 0 or j > 0:
        if i > 0 and s[i - 1, j] == s[i, j]:
            i = i - 1
        elif j > 0 and s[i, j - 1] == s[i, j]:
            j = j - 1
        else:
            i = i - 1
            j = j - weights[i]
            ret.append(i)
    return s[-1, -1], ret


if __name__ == '__main__':
    weights = [1, 2, 4, 4, 6]
    prices = [4, 7, 9, 6, 12]
    W = 10
    p, r = ruksak(weights, prices, W)

    print(p)
    for i in r:
        print(weights[i], prices[i])

"""
L = len(weights)
O(W*L)

    0   1   2   3   4   5   6   ... W
0   0   0   0   0   0   0   0   ... 0
1,4 0   4   4   4   4   4   4   ... 4
2,7 0   4   7   11  11  11  11  ... 11
4,9 0   4   7   11  11  13  16  ... 20

    s[n][W] 
    s[n][W] = max(s[n-1][W], s[n][W-1],
                s[n-1][W-w[n]] + p[n])


"""
