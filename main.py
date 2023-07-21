board_list = ["Algebra", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_player = 'X'


def introduction():
    print('-------------------------------------------------')
    print('-----   Krizic - Kruzic [ Terminal igra ]   -----')
    print('-------------------------------------------------')
    print('Odaberite broj 1 - 9 za postavljanje \'X\' ili \'O\'\n')


def draw_board():
    print(
        f' {board_list[1]} | {board_list[2]} | {board_list[3]}\n'
        f'---|---|---\n'
        f' {board_list[4]} | {board_list[5]} | {board_list[6]}\n'
        f'---|---|---\n'
        f' {board_list[7]} | {board_list[8]} | {board_list[9]}'
    )


def gameplay():
    global current_player

    while True:
        print(f'Trenutno igra: {current_player}\n')
        draw_board()

        board_position = int(input('>> '))
        if board_list[board_position] == ' ':
            board_list[board_position] = current_player
        else:
            print('Celija je zauzeta, odaberite drugo polje')

        if (board_list[1] == board_list[2] == board_list[3] != ' ' or
            board_list[4] == board_list[5] == board_list[6] != ' ' or
            board_list[7] == board_list[8] == board_list[9] != ' ' or
            board_list[1] == board_list[4] == board_list[7] != ' ' or
            board_list[2] == board_list[5] == board_list[8] != ' ' or
            board_list[3] == board_list[6] == board_list[9] != ' ' or
            board_list[1] == board_list[5] == board_list[9] != ' ' or
                board_list[3] == board_list[5] == board_list[7] != ' '):
            print(f'Igra je gotova! \'{current_player}\' pobjeduje!')
            print('Zelite li ponovno igrati? "D(Da) / N(Ne)"')

            restart_input = input('>> ').upper()
            if restart_input == 'D':
                restart()

        elif ' ' not in board_list:
            print('Igra je gotova! Izjednaceno!')
            print('Zelite li ponovno igrati? "D(Da) / N(Ne)"')

            restart_input = input('>> ').upper()
            if restart_input == 'D':
                restart()

        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'


def restart():
    global board_list
    board_list = ["Algebra", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    gameplay()


introduction()
gameplay()
