try:
   # try:
        1//0
#    except ZeroDivisionError:
        print("Zero dividing")
  #      raise Exception('ошибка произошла при вычислении чего-то важного')
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
    print(type(e))
    print('Не деление на ноль, а что-то ещё')
    #raise
