def simplerange():
    print('Start iteration')
    yield 0
    yield 1
    yield 2
    return 4
    yield 3

print(simplerange())

for i in simplerange():
    print(i)

def double(a):
    for x in a:
        yield x
        yield x

for i in double([1, 2, 3]):
    print(i)

def nrang(a):
    i = 0
    while i < a:
        yield i
        i = i + 1

def nrange(s, a):
    i = s
    while i < a:
        yield i
        i = i + 1


print("nrange test")
for a in nrang(5):
    print(a)
for a in nrange(1, 3):
    print(a)


def cumsum(a):
    sum = 0
    for x in a:
        sum += x
        yield sum


print(list(cumsum(range(5))))