def binary_search_between(where, what, start, end):
    '''
    Бинарный поиск положения what в where, номер больше или равен start и номер меньше или равен end.
    '''
    if start==end: # проверка на схлопнувшееся место
        return start
    pos = (start + end)//2 # целочисленное деление, округление вниз
    val = where[pos]
    if val==what: # нашли значение, возвращаем его положение
        return pos
    elif what<val: # в левой половине
        return binary_search_between(where, what, start, pos)
    else: # в правой половине
        return binary_search_between(where, what, pos, end)

def binary_search(where, what):
    '''
    Бинарный поиск положения what в where.
    '''
    return binary_search_between(where, what, 0, len(where))


if __name__=='__main__':
    a = [3, 6, 8, 9, 10, 11, 12, 23, 37]
    for i in a:
        pos = binary_search(a, i)
        print('found', i, 'in', pos, 'position',sep=' ')