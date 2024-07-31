# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lilly Woodward
#               Kyle Rex
#               Jesse Garcia
#               Ethan Nugyen
# Section:      516
# Assignment:   Lab 7
# Date:         10 12 2022
x = 0  # Initializes variable for iterations
# Assigns the board by rows to make looping neater
board = [['1', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['2', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['3', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['4', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['6', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['7', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['8', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['9', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

play = input('Type "play" to continue the game or "stop" to end the game. ')  # Allows for user to start and stop playing whenever
print("   1  2  3  4  5  6  7  8  9")  # Aligns columns for better readability
for i in range(len(board)):  # Prints out the elements of the list 'board' into something visually convenient
    x = 0
    for j in board[i]:  # Prints out elements of elements inside of list 'board'
        print(board[i][x], end='  ')
        x += 1
    print('')

count = 0  # Initializes count for iteration (Determines who's turn it is)
while (play != 'stop') or count != 81:  # Runs loop until the board is full or user enters stop
    if count % 2 == 0:  # Decides Black's turn
        print('Place your black stone')
        row_inputstr = input('Enter row number: ')
        if row_inputstr == 'stop':
            print('The game has ended.')
            break
        row_input = int(row_inputstr)
        column_inputstr = input('Enter column number: ')
        if column_inputstr == 'stop':
            print('The game has ended.')
            break
        column_input = int(column_inputstr)
        count += 1

        if (board[row_input - 1][column_input] == '*' or board[row_input - 1][column_input] == '@'):  # Checks if spot is available
            print('This spot is taken, try again')
            row_input = int(input('Enter row number: '))
            column_input = int(input('Enter column number: '))
        board[row_input - 1][column_input] = '*'
    else:  # Decides White's turn
        print('Place your white stone')
        row_inputstr = input('Enter row number: ')
        if (row_inputstr == 'stop'):
            print('The game has ended.')
            break
        row_input = int(row_inputstr)
        column_inputstr = input('Enter column number: ')
        if (column_inputstr == 'stop'):
            print('The game has ended.')
            break
        column_input = int(column_inputstr)
        count += 1

        if (board[row_input - 1][column_input] == '*' or board[row_input - 1][column_input] == '@'):  # Checks if spot is available
            print('This spot is taken, try again')
            row_input = int(input('Enter row number: '))
            column_input = int(input('Enter column number: '))
        board[row_input - 1][column_input] = '@'
    print("   1  2  3  4  5  6  7  8  9")  # Aligns columns for every board while user is playing
    for i in range(len(board)):  # Prints out new board with updated elements after every turn
        x = 0
        for j in board[i]:
            print(board[i][x], end='  ')
            x += 1
        print('')
    if play == 'stop':
        break