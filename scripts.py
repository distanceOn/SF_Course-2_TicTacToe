field = list(range(1,10))

combinations = [(1,2,3), (4,5,6), (7,8,9),(1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

def render_field():
    print('    0 1 2')
    print('  -------')
    for i in range(3):
        print(i, '|',  field[0 + i*3],  field[1 + i*3],  field[2 + i*3])

def take_sign(sign):
    while True:
        value = input('Сейчас ходит ' + sign + '. Выбирайте номер клетки ')
        if not (value in '123456789'):
            print('Повторите ввод, значение неверное')
            continue
        value = int(value)
        if str(field[value-1]) in 'XO':
            print('Клетка занята')
            continue
        field[value - 1] = sign
        break

def check_winner():
    for elem in combinations:
        if(field[elem[0]-1]) == (field[elem[1]-1]) == (field[elem[2]-1]):
            return field[elem[1]-1]
    else:
        return False

def play():
    counter = 0
    while True:
        render_field()
        if counter % 2 == 0:
            take_sign('X')
        else:
            take_sign('O')
        if counter > 3:
            winner = check_winner()
            if winner:
                render_field()
                print(winner, 'победил!')
                break
        counter += 1
        if counter > 8:
            render_field()
            print('Ничья')
            break


play()