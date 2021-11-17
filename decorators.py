def my_decorator(func):
    def the_wrapper(*args, **kwargs):
        print("Первый декоратор")
        print("Аргумент ", args)
        print("Аргумент ", kwargs)
        func(*args, **kwargs)
        print("Внутренний декоратор, после функции")
    return the_wrapper

def my_decorator2(func):
    def the_wrapper():
        print("Второй декоратор")
        func()
        print("Наружный декоратор")
    return the_wrapper

def my_decorator3(name):
    def my_decorator_in(func):
        def the_wrapper():
            print("Третий декоратор")
            print("Имя =", name)
            func()
            print("Третий декоратор, после функции")
        return the_wrapper
    return my_decorator_in


@my_decorator
@my_decorator2
def f():
    print("Сообщение")

@my_decorator
def f2(a, b):
    print("Сообщение", a)

@my_decorator3('Питон')
def f3():
    print("Сообщение 3")



if __name__ == '__main__':
#    f()
#    f2("текст", 1)
    f3()
