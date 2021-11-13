COINS = (1, 5, 10)
N = 5

def numberChanges(coins, n):

    return 1

if __name__ == '__main__':
    print(numberChanges(COINS, N))


"""

N 0 1 2 3 4 5 6 7 8 9 10
c 0 1 1 1 1 2 2 2 2 2 4


10 = 1 + 9 ~ 2: 1+4*1+5, 1+9*1
10 = 5 + 5 ~ 2: 5+1*5, 5+5
10 = 10 + 0 ~ 1


"""