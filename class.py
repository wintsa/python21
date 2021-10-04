class Clazz:
    x = 0
    def __init__(self):
        print("init")
        Clazz.x = Clazz.x + 1
        self.id = Clazz.x


print(Clazz.x)
obj1 = Clazz()
obj2 = Clazz()
obj3 = Clazz()
Clazz.x
print(obj1.x)




class Adder:
    x = 5

    def add(self, b):
        self.x = self.x + b.x
        return self.x


adder = Adder()
r = adder.add(Clazz())
print(r)

r = Adder.add(adder, Clazz)
print(r)



f = adder.add
adder.x = 10
f(Clazz)


def makeAdder():
    class result:
        def add(b):
            return Adder.add(result, b)

    return result

