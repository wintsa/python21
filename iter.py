from math import acos


it = iter({3, 6, 8, 2})


def print_all(a):
    i = iter(a)
    try:
        while True:
            print(next(i))
    except StopIteration:
        pass

def print_all_for_iter(i):
    try:
        while True:
            print(next(i))
    except StopIteration:
        pass    

class humanYearIterator:
    def __init__(self, humanObj):
        self.humanObj = humanObj
        self.year = 0
    def __next__(self):
        if self.year < self.humanObj.age:
            result = ""
            if self.year<3:
                result = str(self.year) + ", Yasli "+ self.humanObj.name
            elif self.year<7:
                result = str(self.year) + ", Detsad "+ self.humanObj.name
            elif self.year<18:
                result = str(self.year) + ", School "+ self.humanObj.name
            else:
                result = str(self.year) + ", Work "+ self.humanObj.name
            self.year += 1
            return result
        else:
            raise StopIteration

class human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __iter__(self):
        humanYearIteratorObj = humanYearIterator(self)
        return humanYearIteratorObj
    def __str__(self):
        return "Human: "+self.name + ", age=" + str(self.age)
    def __repr__(self):
        return self.name +"(" + str(self.age)+")"
    def sayHello(self):
        print("Hello,", self.name)



if __name__ == '__main__':
    ivan = human(3, "Ivan")
    ivan.sayHello()
    human.sayHello(ivan)
    for a in ivan:
        print(a)
        '''
    print(ivan)
    ivanYears1 = iter(ivan)
    ivanYears2 = iter(ivan)
    petr = human(9, "Petr")
    print(petr)
    print([ivan, petr])
    petrYears = iter(petr)
    print_all_for_iter(ivanYears1)
    print_all_for_iter(ivanYears2)
    print_all_for_iter(petrYears)'''



print("stop")


from dataclasses import dataclass


@dataclass
class myrangeIteratorClass:
    n: int  # ограничение
    i: int = 0  # счётчик

    def __next__(self):
        if self.i < self.n:
            result = self.i
            self.i += 1
            return result
        else:
            raise StopIteration


class myrangeClass:
    n = 10

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        myrangeIteratorObj = myrangeIteratorClass(self.n)
        return myrangeIteratorObj

    def __str__(self):
        return "myrangeClass: n=" + str(self.n)

    def __repr__(self):
        return "n=" + str(self.n)

    def __add__(self, other):
        if isinstance(other, myrangeClass):
            return myrangeClass(self.n + other.n)
        if isinstance(other, int):
            return myrangeClass(self.n + other)
        raise TypeError


myrangeObject3 = myrangeClass(3)
myrangeObject7 = myrangeClass(7)
myrangeObject10 = myrangeObject3 + myrangeObject7

myrangeObject = myrangeClass(3)
print(myrangeObject)
print([myrangeClass(3), myrangeClass(11), myrangeClass(103)])
print_all(myrangeObject)

for i in myrangeClass(n=5):
    print(i)


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


def nrange(a):
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
for a in nrange(1, 3):
    print(a)


def cumsum(a):
    sum = 0
    for x in a:
        sum += x
        yield sum


print(list(cumsum(simplerange())))
