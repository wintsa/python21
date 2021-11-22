import math


def add(a: int, b: int) -> int:
    """
    Функция складывает два числа
    """
    return a + b

class T:
    x = 0
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if isinstance(other, T):
            return T(self.x + other.x)
        if isinstance(other, int):
            return T(self.x + other)
        return None

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return 'r'+str(self.x)


if __name__ == '__main__':
    """
    # s = {1, 2, 3, 1, 2, 3}
    l = [1, 2, 3, 1, 2, 3]
    t = (1, 2, 3, 1, 2, 3)

    s = set(l)
    l.append(2)
    print(s, l, t)
    a = False or True and False or True
    print(a)
    """
    '''l = [input(), input()]
    a, b = map(int, l)
    print(add(a,b))'''

    a = T(3)
    b = T(4)
    c = a + b
    d = a + 5
    print(c, d)
    print([c, d])