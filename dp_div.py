def numberWays(n):
    nways = list(range(n))
    nways[0] = 1
    for i in range(1, n):
        nways[i] = nways[i - 1]
        pos = i + 1
        if pos % 2 == 0:
            nways[i] += nways[pos // 2 - 1]
        if pos % 3 == 0:
            nways[i] += nways[pos // 3 - 1]
    return nways[n - 1]

def appendStep(ways, step):
    ret_ways = list()
    if len(ways)==0:
        ret_way = list()
        ret_way.append(step)
        ret_ways.append(ret_way)
        return ret_ways
    for way in ways:
        ret_way = list(way)
        ret_way.append(step)
        ret_ways.append(ret_way)
    return ret_ways

def appendWay(ways1, ways2):
    ret_ways = list()
    for way in ways1:
        ret_ways.append(way)
    for way in ways2:
        ret_ways.append(way)
    return ret_ways

def minWays(n):
    minways = list(range(n))
    minways[0] = 0
    ways = list(range(n))
    ways[0] = list()
    for i in range(1, n):
        minways[i] = minways[i - 1] + 1
        ways[i] = appendStep(ways[i - 1], '-1')
        pos = i + 1
        if pos % 2 == 0:
            pos_old = pos // 2 - 1
            if minways[i] > minways[pos_old] + 1:
                minways[i] = minways[pos_old] + 1
                ways[i] = appendStep(ways[pos_old], '/2')
            elif minways[i] == minways[pos_old] + 1:
                new_way = appendStep(ways[pos_old], '/2')
                ways[i] = appendWay(ways[i], new_way)
        if pos % 3 == 0:
            pos_old = pos // 3 - 1
            if minways[i] > minways[pos_old] + 1:
                minways[i] = minways[pos_old] + 1
                ways[i] = appendStep(ways[pos_old], '/3')
            elif minways[i] == minways[pos_old] + 1:
                new_way = appendStep(ways[pos_old], '/3')
                ways[i] = appendWay(ways[i], new_way)
#    print(minways)
    return ways[n - 1]


if __name__ == '__main__':
    print(minWays(10))

"""

N
-1 
/2 if div 2
/3 if div 3
to 1 how many ways?

i 0 1 2 3
N 1 2 3 4 5 6  7
c 1 2 3 5 5 10 10

i   0   1   2   3
N   1   2   3   4   5   6   7   8
d   0   1   1   2   3   2   3   3
m   0  /2  /3   /2/2
                -1/3
"""
