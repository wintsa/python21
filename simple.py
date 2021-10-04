def add(a, b):
    return a+b

if __name__=='__main__':
    l = [input(), input()]
    a, b = map(int, l)
    print(add(a,b))