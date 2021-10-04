def test():
    return 1//0


def test2():
    raise TypeError('Some Error')
    return int("12q")

def test3():
    return test2()


try:
    test3()
except ZeroDivisionError as e:
    print("incorrect zero")
except ValueError as e:
    print("incorrect value")
except Exception as e:
    print("general Exception:", e)

print("Good")