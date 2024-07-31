# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lilly Woodward
#               Kyle Rex
#               Jesse Garcis
# Section:      516
# Assignment:   Project
# Date:         5 12 2022

import random as rd
counter = rd.randint(0,1)
valid_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', ]
board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
play_again = ''
x_wins = 0
o_wins = 0
player_wins = 0
bot_wins = 0
draw_counter = 0
bot_draw_counter = 0
prev_count = 0
print('Match 3 in a row to win...')


def next_move():
    global counter
    global prev_count
    if counter % 2 == 0:
        next_move0 = input('O to move, enter row and column (ie: A1): ').lower()
        while next_move0 not in valid_moves:
            next_move0 = input('Invalid move! X to move, enter row and column (ie: A1): ').lower()
        valid_moves.remove(next_move0)
    else:
        next_move0 = input('X to move, enter row and column (ie: A1): ').lower()
        while next_move0 not in valid_moves:
            next_move0 = input('Invalid move! X to move, enter row and column (ie: A1): ').lower()
        valid_moves.remove(next_move0)
    counter += 1
    prev_count += 1
    return next_move0


def bot_move():
    global counter
    if len(valid_moves) != 0:
        bot_move0 = rd.randint(0, len(valid_moves) - 1)
        saved_move = valid_moves[bot_move0]
        print()
        print(f'The bot has played {saved_move}')
        counter += 1
        valid_moves.remove(valid_moves[bot_move0])
        return saved_move


def bot_move_hard():
    global counter
    global prev_count
    counter += 1
    if len(valid_moves) != 0:
        if counter % 2 == 1 and prev_count == 1:
            if board[0][0] != ' ' or board[2][0] != ' ' or board[2][2] != ' ' or board[0][2] != ' ':
                bot_move_hard0 = 'b2'
            elif board[1][1] != ' ':
                bot_move_hard0 = rd.choice(['a1', 'c1', 'c3', 'a3'])
            else:
                bot_move_hard0 = rd.choice(valid_moves)

        elif counter % 2 == 0 and prev_count == 0:
            bot_move_hard0 = rd.choice(['a1', 'c1', 'c3', 'a3', 'b2'])

        else:
            for i in range(len(board)):
                if counter % 2 == 1:
                    if board[i][0] == 'O' and board[i][2] == 'O' and board[i][1] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a2'
                        elif i == 1:
                            bot_move_hard0 = 'b2'
                        elif i == 2:
                            bot_move_hard0 = 'c2'
                        break
                    elif board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a3'
                        elif i == 1:
                            bot_move_hard0 = 'b3'
                        elif i == 2:
                            bot_move_hard0 = 'c3'
                        break
                    elif board[i][1] == 'O' and board[i][2] == 'O' and board[i][0] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a1'
                        elif i == 1:
                            bot_move_hard0 = 'b1'
                        elif i == 2:
                            bot_move_hard0 = 'c1'
                        break
                    ################
                    elif board[1][i] == 'O' and board[2][i] == 'O' and board[0][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a1'
                        elif i == 1:
                            bot_move_hard0 = 'a2'
                        elif i == 2:
                            bot_move_hard0 = 'a3'
                        break
                    elif board[1][i] == 'O' and board[0][i] == 'O' and board[2][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'c1'
                        elif i == 1:
                            bot_move_hard0 = 'c2'
                        elif i == 2:
                            bot_move_hard0 = 'c3'
                        break
                    elif board[0][i] == 'O' and board[2][i] == 'O' and board[1][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'b1'
                        elif i == 1:
                            bot_move_hard0 = 'b2'
                        elif i == 2:
                            bot_move_hard0 = 'b3'
                        break
                    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == ' ':
                        bot_move_hard0 = 'c3'
                        break
                    elif board[0][0] == 'O' and board[2][2] == 'O' and board[1][1] == ' ':
                        bot_move_hard0 = 'b2'
                        break
                    elif board[2][2] == 'O' and board[1][1] == 'O' and board[0][0] == ' ':
                        bot_move_hard0 = 'a1'
                        break
                    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == ' ':
                        bot_move_hard0 = 'c1'
                        break
                    elif board[0][2] == 'O' and board[2][0] == 'O' and board[1][1] == ' ':
                        bot_move_hard0 = 'b2'
                        break
                    elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == ' ':
                        bot_move_hard0 = 'a3'
                        break
                    elif board[i][0] == 'X' and board[i][2] == 'X' and board[i][1] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a2'
                        elif i == 1:
                            bot_move_hard0 = 'b2'
                        elif i == 2:
                            bot_move_hard0 = 'c2'
                        break
                    elif board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a3'
                        elif i == 1:
                            bot_move_hard0 = 'b3'
                        elif i == 2:
                            bot_move_hard0 = 'c3'
                        break
                    elif board[i][1] == 'X' and board[i][2] == 'X' and board[i][0] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a1'
                        elif i == 1:
                            bot_move_hard0 = 'b1'
                        elif i == 2:
                            bot_move_hard0 = 'c1'
                        break
                    elif board[1][i] == 'X' and board[2][i] == 'X' and board[0][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a1'
                        elif i == 1:
                            bot_move_hard0 = 'a2'
                        elif i == 2:
                            bot_move_hard0 = 'a3'
                        break
                    elif board[1][i] == 'X' and board[0][i] == 'X' and board[2][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'c1'
                        elif i == 1:
                            bot_move_hard0 = 'c2'
                        elif i == 2:
                            bot_move_hard0 = 'c3'
                        break
                    elif board[0][i] == 'X' and board[2][i] == 'X' and board[1][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'b1'
                        elif i == 1:
                            bot_move_hard0 = 'b2'
                        elif i == 2:
                            bot_move_hard0 = 'b3'
                        break
                    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == ' ':
                        bot_move_hard0 = 'c3'
                        break
                    elif board[0][0] == 'X' and board[2][2] == 'X' and board[1][1] == ' ':
                        bot_move_hard0 = 'b2'
                        break
                    elif board[2][2] == 'X' and board[1][1] == 'X' and board[0][0] == ' ':
                        bot_move_hard0 = 'a1'
                        break
                    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == ' ':
                        bot_move_hard0 = 'c1'
                        break
                    elif board[0][2] == 'X' and board[2][0] == 'X' and board[1][1] == ' ':
                        bot_move_hard0 = 'b2'
                        break
                    elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == ' ':
                        bot_move_hard0 = 'a3'
                        break
                    else:
                        bot_move_hard0 = rd.choice(valid_moves)
                else:
                    if board[i][0] == 'X' and board[i][2] == 'X' and board[i][1] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a2'
                        elif i == 1:
                            bot_move_hard0 = 'b2'
                        elif i == 2:
                            bot_move_hard0 = 'c2'
                        break
                    elif board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a3'
                        elif i == 1:
                            bot_move_hard0 = 'b3'
                        elif i == 2:
                            bot_move_hard0 = 'c3'
                        break
                    elif board[i][1] == 'X' and board[i][2] == 'X' and board[i][0] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a1'
                        elif i == 1:
                            bot_move_hard0 = 'b1'
                        elif i == 2:
                            bot_move_hard0 = 'c1'
                        break
                    elif board[1][i] == 'X' and board[2][i] == 'X' and board[0][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a1'
                        elif i == 1:
                            bot_move_hard0 = 'a2'
                        elif i == 2:
                            bot_move_hard0 = 'a3'
                        break
                    elif board[1][i] == 'X' and board[0][i] == 'X' and board[2][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'c1'
                        elif i == 1:
                            bot_move_hard0 = 'c2'
                        elif i == 2:
                            bot_move_hard0 = 'c3'
                        break
                    elif board[0][i] == 'X' and board[2][i] == 'X' and board[1][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'b1'
                        elif i == 1:
                            bot_move_hard0 = 'b2'
                        elif i == 2:
                            bot_move_hard0 = 'b3'
                        break
                    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == ' ':
                        bot_move_hard0 = 'c3'
                        break
                    elif board[0][0] == 'X' and board[2][2] == 'X' and board[1][1] == ' ':
                        bot_move_hard0 = 'b2'
                        break
                    elif board[2][2] == 'X' and board[1][1] == 'X' and board[0][0] == ' ':
                        bot_move_hard0 = 'a1'
                        break
                    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == ' ':
                        bot_move_hard0 = 'c1'
                        break
                    elif board[0][2] == 'X' and board[2][0] == 'X' and board[1][1] == ' ':
                        bot_move_hard0 = 'b2'
                        break
                    elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == ' ':
                        bot_move_hard0 = 'a3'
                        break
                    elif board[i][0] == 'O' and board[i][2] == 'O' and board[i][1] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a2'
                        elif i == 1:
                            bot_move_hard0 = 'b2'
                        elif i == 2:
                            bot_move_hard0 = 'c2'
                        break
                    elif board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a3'
                        elif i == 1:
                            bot_move_hard0 = 'b3'
                        elif i == 2:
                            bot_move_hard0 = 'c3'
                        break
                    elif board[i][1] == 'O' and board[i][2] == 'O' and board[i][0] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a1'
                        elif i == 1:
                            bot_move_hard0 = 'b1'
                        elif i == 2:
                            bot_move_hard0 = 'c1'
                        break
                    elif board[1][i] == 'O' and board[2][i] == 'O' and board[0][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'a1'
                        elif i == 1:
                            bot_move_hard0 = 'a2'
                        elif i == 2:
                            bot_move_hard0 = 'a3'
                        break
                    elif board[1][i] == 'O' and board[0][i] == 'O' and board[2][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'c1'
                        elif i == 1:
                            bot_move_hard0 = 'c2'
                        elif i == 2:
                            bot_move_hard0 = 'c3'
                        break
                    elif board[0][i] == 'O' and board[2][i] == 'O' and board[1][i] == ' ':
                        if i == 0:
                            bot_move_hard0 = 'b1'
                        elif i == 1:
                            bot_move_hard0 = 'b2'
                        elif i == 2:
                            bot_move_hard0 = 'b3'
                        break
                    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == ' ':
                        bot_move_hard0 = 'c3'
                        break
                    elif board[0][0] == 'O' and board[2][2] == 'O' and board[1][1] == ' ':
                        bot_move_hard0 = 'b2'
                        break
                    elif board[2][2] == 'O' and board[1][1] == 'O' and board[0][0] == ' ':
                        bot_move_hard0 = 'a1'
                        break
                    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == ' ':
                        bot_move_hard0 = 'c1'
                        break
                    elif board[0][2] == 'O' and board[2][0] == 'O' and board[1][1] == ' ':
                        bot_move_hard0 = 'b2'
                        break
                    elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == ' ':
                        bot_move_hard0 = 'a3'
                        break
                    else:
                        bot_move_hard0 = rd.choice(valid_moves)
        saved_move_hard = bot_move_hard0
        print(f'The bot has played {saved_move_hard}')
        valid_moves.remove(bot_move_hard0)
        return saved_move_hard


def detect_win():
    global winner
    for i in range(len(board)):
        if board[i][0] != ' ':
            if board[i][0] == board[i][1] == board[i][2]:
                winner = f'{board[i][0]}'
        if board[0][i] != ' ':
            if board[0][i] == board[1][i] == board[2][i]:
                winner = f'{board[0][i]}'

    if board[0][0] != ' ':
        if board[0][0] == board[1][1] == board[2][2]:
            winner = f'{board[0][0]}'
    if board[2][0] != ' ':
        if board[2][0] == board[1][1] == board[0][2]:
            winner = f'{board[2][0]}'
    return winner


def show_board(x):
    if counter % 2 == 1:
        if x == 'a1':
            board[0][0] = 'O'
        elif x == 'a2':
            board[0][1] = 'O'
        elif x == 'a3':
            board[0][2] = 'O'
        elif x == 'b1':
            board[1][0] = 'O'
        elif x == 'b2':
            board[1][1] = 'O'
        elif x == 'b3':
            board[1][2] = 'O'
        elif x == 'c1':
            board[2][0] = 'O'
        elif x == 'c2':
            board[2][1] = 'O'
        elif x == 'c3':
            board[2][2] = 'O'
    else:
        if x == 'a1':
            board[0][0] = 'X'
        elif x == 'a2':
            board[0][1] = 'X'
        elif x == 'a3':
            board[0][2] = 'X'
        elif x == 'b1':
            board[1][0] = 'X'
        elif x == 'b2':
            board[1][1] = 'X'
        elif x == 'b3':
            board[1][2] = 'X'
        elif x == 'c1':
            board[2][0] = 'X'
        elif x == 'c2':
            board[2][1] = 'X'
        elif x == 'c3':
            board[2][2] = 'X'

    row_count = ['A', 'B', 'C']
    row_counter = 0
    print()
    print('     1     2     3')
    for row in range(len(board)):
        board_print = '  ' + row_count[row_counter] + '  '
        for element in range(len(board[row])):
            if element < 2:
                board_print += board[row][element] + '  |  '
            else:
                board_print += board[row][element]
        print(board_print)
        if row < 2:
            print('    ---------------')
            row_counter += 1
    print()


def clear_board():
    global valid_moves
    global board
    global game_status
    global winner
    valid_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', ]
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    game_status = ''
    winner = ''


def play_game():
    global x_wins
    global o_wins
    global draw_counter
    global game_status
    global winner

    clear_board()
    show_board('')
    while game_status != 'finished':
        show_board(next_move())
        for i in range(len(board)):
            if board[i][0] != ' ':
                if board[i][0] == board[i][1] == board[i][2]:
                    winner = f'{board[i][0]}'
            if board[0][i] != ' ':
                if board[0][i] == board[1][i] == board[2][i]:
                    winner = f'{board[0][i]}'

        if board[0][0] != ' ':
            if board[0][0] == board[1][1] == board[2][2]:
                winner = f'{board[0][0]}'
        if board[2][0] != ' ':
            if board[2][0] == board[1][1] == board[0][2]:
                winner = f'{board[0][0]}'

        if winner != '':
            game_status = 'finished'
            print(f'{winner} has won the game!')
            print()
            if winner == 'X':
                x_wins += 1
            else:
                o_wins += 1
        elif len(valid_moves) == 0:
            game_status = 'finished'
            print('There are no valid moves left, it is a draw.')
            draw_counter += 1
            print()


def play_robot_easy():
    global player_wins
    global bot_wins
    global bot_draw_counter
    global counter
    global game_status
    global winner

    clear_board()
    player_decision = input('Would you like to play X\'s or O\'s? X starts first (Enter "X" or "O"): ')

    if player_decision == 'X':
        show_board('')
        while game_status != 'finished':
            if counter % 2 == 0:
                counter += 1
                continue
            show_board(next_move())
            detect_win()
            if detect_win() == 'X' or detect_win() == 'O':
                if winner != '':
                    game_status = 'finished'
                    print(f'{winner} has won the game!')
                    print()
                    if winner == 'X':
                        if player_decision == 'X':
                            player_wins += 1
                        else:
                            bot_wins += 1
                    else:
                        if player_decision == 'X':
                            bot_wins += 1
                        else:
                            player_wins += 1
                    break
            elif len(valid_moves) == 0:
                game_status = 'finished'
                print('There are no valid moves left, it is a draw.')
                bot_draw_counter += 1
                print()
                break
            show_board(bot_move())
            detect_win()
            if detect_win() == 'X' or detect_win() == 'O':
                if winner != '':
                    game_status = 'finished'
                    print(f'{winner} has won the game!')
                    print()
                    if winner == 'X':
                        if player_decision == 'X':
                            player_wins += 1
                        else:
                            bot_wins += 1
                    else:
                        if player_decision == 'X':
                            bot_wins += 1
                        else:
                            player_wins += 1
                    break
            elif len(valid_moves) == 0:
                game_status = 'finished'
                print('There are no valid moves left, it is a draw.')
                bot_draw_counter += 1
                print()
                break
    else:
        while game_status != 'finished':
            if counter % 2 == 0:
                counter += 1
                continue
            show_board(bot_move())
            detect_win()
            if detect_win() == 'X' or detect_win() == 'O':
                if winner != '':
                    game_status = 'finished'
                    print(f'{winner} has won the game!')
                    print()
                    if winner == 'X':
                        if player_decision == 'X':
                            player_wins += 1
                        else:
                            bot_wins += 1
                    else:
                        if player_decision == 'X':
                            bot_wins += 1
                        else:
                            player_wins += 1
                    break
            elif len(valid_moves) == 0:
                game_status = 'finished'
                print('There are no valid moves left, it is a draw.')
                bot_draw_counter += 1
                print()
                break
            show_board(next_move())
            detect_win()
            if detect_win() == 'X' or detect_win() == 'O':
                if winner != '':
                    game_status = 'finished'
                    print(f'{winner} has won the game!')
                    print()
                    if winner == 'X':
                        if player_decision == 'X':
                            player_wins += 1
                        else:
                            bot_wins += 1
                    else:
                        if player_decision == 'X':
                            bot_wins += 1
                        else:
                            player_wins += 1
                    break
            elif len(valid_moves) == 0:
                game_status = 'finished'
                print('There are no valid moves left, it is a draw.')
                bot_draw_counter += 1
                print()
                break


def play_robot_med():
    global player_wins
    global bot_wins
    global bot_draw_counter
    global counter
    global game_status
    global winner
    global prev_count

    clear_board()
    player_decision = input('Would you like to play X\'s or O\'s? X starts first (Enter "X" or "O"): ')
    if player_decision == 'X':
        show_board('')
        counter = 0
        prev_count = 0
        while game_status != 'finished':
            if counter % 2 == 0:
                counter += 1
                continue
            show_board(next_move())
            detect_win()
            if detect_win() == 'X' or detect_win() == 'O':
                if winner != '':
                    game_status = 'finished'
                    print(f'{winner} has won the game!')
                    print()
                    if winner == 'X':
                        if player_decision == 'X':
                            player_wins += 1
                        else:
                            bot_wins += 1
                    else:
                        if player_decision == 'X':
                            bot_wins += 1
                        else:
                            player_wins += 1
                    break
            elif len(valid_moves) == 0:
                game_status = 'finished'
                print('There are no valid moves left, it is a draw.')
                bot_draw_counter += 1
                print()
                break
            show_board(bot_move_hard())
            detect_win()
            if detect_win() == 'X' or detect_win() == 'O':
                if winner != '':
                    game_status = 'finished'
                    print(f'{winner} has won the game!')
                    print()
                    if winner == 'X':
                        if player_decision == 'X':
                            player_wins += 1
                        else:
                            bot_wins += 1
                    else:
                        if player_decision == 'X':
                            bot_wins += 1
                        else:
                            player_wins += 1
                    break
            elif len(valid_moves) == 0:
                game_status = 'finished'
                print('There are no valid moves left, it is a draw.')
                bot_draw_counter += 1
                print()
                break
    else:
        counter = 0
        prev_count = 0
        while game_status != 'finished':
            if counter % 2 == 0:
                counter += 1
                continue
            show_board(bot_move_hard())
            detect_win()
            if detect_win() == 'X' or detect_win() == 'O':
                if winner != '':
                    game_status = 'finished'
                    print(f'{winner} has won the game!')
                    print()
                    if winner == 'X':
                        if player_decision == 'X':
                            player_wins += 1
                        else:
                            bot_wins += 1
                    else:
                        if player_decision == 'X':
                            bot_wins += 1
                        else:
                            player_wins += 1
                    break
            elif len(valid_moves) == 0:
                game_status = 'finished'
                print('There are no valid moves left, it is a draw.')
                bot_draw_counter += 1
                print()
                break
            show_board(next_move())
            detect_win()
            if detect_win() == 'X' or detect_win() == 'O':
                if winner != '':
                    game_status = 'finished'
                    print(f'{winner} has won the game!')
                    print()
                    if winner == 'X':
                        if player_decision == 'X':
                            player_wins += 1
                        else:
                            bot_wins += 1
                    else:
                        if player_decision == 'X':
                            bot_wins += 1
                        else:
                            player_wins += 1
                    break
            elif len(valid_moves) == 0:
                game_status = 'finished'
                print('There are no valid moves left, it is a draw.')
                bot_draw_counter += 1
                print()
                break



play_decision = input('Would you like to play against a bot or a player? (Enter bot/player): ').lower()

while play_decision != 'player' and play_decision != 'bot':
    try:
        play_decision = input('Bad input! Would you like to play against a bot or a player? (Enter bot/player): ').lower()
    except:
        pass

if play_decision == 'player':
    while play_again != 'n':
        play_game()
        play_again = input('Would you like to play again? (Y/N): ').lower()
    print()
    print('O: ' + str(o_wins))
    print('X: ' + str(x_wins))
    print('Draws: ' + str(draw_counter))
elif play_decision == 'bot':
    easy_or_hard = input('Which difficulty? (Easy/Med): ').lower()
    if easy_or_hard == 'easy':
        while play_again != 'n':
            play_robot_easy()
            play_again = input('Would you like to play again? (Y/N): ').lower()
    elif easy_or_hard == 'med':
        while play_again != 'n':
            play_robot_med()
            play_again = input('Would you like to play again? (Y/N): ').lower()
    print()
    print('Player: ' + str(player_wins))
    print('Robot: ' + str(bot_wins))
    print('Draws: ' + str(bot_draw_counter))
