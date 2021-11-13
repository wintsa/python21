cnt = 0
def f(i):
    global cnt
    cnt += 1
    if i<2:
        return 1
    return f(i-1) + f(i-2)


fib_mem = dict()
"""
def fib(i):
    global cnt
    if i == 0 or i == 1:
        return 1
    cnt += 1
    val = fib_mem.get(i, None)
    if val is None:
        val = fib(i - 1) + fib(i - 2)
        fib_mem[i] = val
    return val

"""

def fib(i):
    global cnt
    fib_mem = {0: 1, 1: 1}
    for a in range(2, i + 1):
        cnt += 1
        fib_mem[a] = fib_mem[a - 2] + fib_mem[a - 1]
    return fib_mem[i]


if __name__ == '__main__':
    print(fib(100))
    print(cnt)
"""
    a = [1, 3, 1]
    print(len(a))
    s = set()
    s.add(3)
    s.add(3)
    s.add(5)
    s.add(3)
    print(s)
    print(fib(11))
    print(cnt)
"""



"""
0 1 2 3 4 5 6
1 1 2 3 5 8 13

f[n] = f[n-1] + f[n-2]
"""
