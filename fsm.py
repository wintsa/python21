def menu(a: str):
    if a == 'echo':
        return echo
    elif a == 'div2':
        return div2
    elif a == 'exit':
        return None
    print('Unexpected type')
    return menu

def div2(a: str):
    try:
        if int(a) % 2 == 0:
            print('even')
        else:
            print('odd')
    except:
        print('Not a number')
    return menu


def echo(a: str):
    print(a)
    return menu

'''
def run():
    state = menu
    for a in ['echo', 'test', 'div2', '5']:
        state = state(a)
'''

if __name__=='__main__':
    print('Введите "echo" для эхо или "div2" чтобы узнать, чётно ли число или "exit" для выхода')
    st = menu
    while st != None:
        st = st(input())
