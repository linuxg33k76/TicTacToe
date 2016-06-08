'''
Python Tic Tac Toe Game
Ben Calvert
June 7, 2016
'''

# Global Variables

board = [1,2,3,4,5,6,7,8,9]
gameover = False

# Functions

def print_board(layout):
    '''
    This will print out a board based on the passed board variable
    :param layout:
    :return: nothing
    '''
    print('Here is the board')
    print('\n')
    print(str(layout[0]) + '|'+ str(layout[1]) + '|' + str(layout[2]))
    print('-----')
    print(str(layout[3]) + '|'+ str(layout[4]) + '|' + str(layout[5]))
    print('-----')
    print(str(layout[6]) + '|'+ str(layout[7]) + '|' + str(layout[8]))
    print('\n')

def check(b,mark,player):
    '''
    This function checks to see if there is a Tic Tac Toe based on player and player's mark.
    If no winner and all the spaces are used, then it ends the game by setting gameover to True.
    Check list:
    1.) across the top
    2.) across the middle
    3.) across the bottom
    4.) down the left side
    5.) down the middle
    6.) down the right side
    7.) diagonal top left to bottom right
    8.) diagonal top right to bottom left
    :param b:
    :param mark:
    :param player:
    :return:
    '''
    if (b[0] == b[1] == b[2] == mark)\
            or (b[3] == b[4] == b[5] == mark) \
            or (b[6] == b[7] == b[8] == mark) \
            or (b[0] == b[3] == b[6] == mark) \
            or (b[1] == b[4] == b[7] == mark) \
            or (b[2] == b[5] == b[8] == mark) \
            or (b[0] == b[4] == b[8] == mark) \
            or (b[2] == b[4] == b[6] == mark):
            global gameover
            gameover = True
            return True
    else:
        if set(b) == set(['X','O']):
            print('Cat and Mouse Game.')
            gameover = True
            return
        else:
            pass

def move(mark,p):
    '''
    This function checks to see if a space is already taken and if there is a valid input.
    If so, then it places a mark based on player's mark.
    :param mark:
    :param p:
    :return:
    '''
    board_pos = raw_input('Please enter a number 1 - 9 that is available: ')
    board_pos = int(board_pos)-1
    if board_pos in range(0,10):
        if board[board_pos] == 'X' or board[board_pos] == 'O':
            print('Choose again! Space already taken.')
            return
        else:
            board[board_pos] = mark
            return
    else:
        print('Chose again!  Not a valid entry.')
        if p == 1:
            p1()
        else:
            p2()
        return

def p1():
    '''
    Player 1 function.  Contains code associated with player 1's moves.
    Gets input from check() in order to print Winner banner.
    :return:
    '''
    print(player_1 + ', please select a position.')
    move('X',1)
    if check(board,'X',player_1) == True:
        print(player_1 + ' is the Winner!')
        print_board(board)
    else:
        return

def p2():
    '''
    Player 2 function.  Contains code associated with player 2's moves.
    Gets input from check() in order to print Winner banner.
    :return:
    '''
    print(player_2 + ', please select a position.')
    move('O',2)
    if check(board,'O',player_2) == True:
        print(player_2 + ' is the Winner!')
        print_board(board)
    else:
        return

# Get Player Information

print('Player 1, please enter your name.')
player_1 = raw_input()
print('Thank you, ' + player_1 + '.  You will be X.')
print('Player 2, please enter your name.')
player_2 = raw_input()
print('Thank you, ' + player_2 + '.  You will be O.')

# Get Player Input - as long as gameover is False

while gameover is False:
    print_board(board)
    p1()
    if gameover is True:
        break
    else:
        print_board(board)
        p2()


