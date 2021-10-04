def menu(a: str):
    print('Введите "echo" для эхо или "div2" чтобы узнать, чётно ли число')
    if a == 'echo':
        return echo
    if a == 'div2':
        return div2
    else:
        return menu

def div2(a: str):
    if int(a) % 2 == 0:
        print('even')
        return menu
    else:
        print('odd')
        return menu


def echo(a: str):
    print(a)
    return menu


def run(input: list):
    state = menu
    for a in ['echo', 'test', 'div2', '5']:
        state = state(a)

run([1,2,3,4])
