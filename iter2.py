def cumfun(a, fun):
    iterator = iter(a)
    result = next(iterator)
    try:
        while True:
            yield result
            result = fun(result, next(iterator))
    except StopIteration: # if type(exception) == StopIteration:
        pass
def add(x,y):
    return x+y
print(list(cumfun(range(5), fun=add)))
print(list(cumfun(range(1,5), fun=lambda x,y: x*y)))
