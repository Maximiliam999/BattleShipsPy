from random import randint

HIDDEN_BOARD = [[' '] * 5 for x in range(5)]
GUESS_BOARD = [[' '] * 5 for x in range(5)]


def print_board(board):
    """
    Print board to terminal.  
    """
    row_number = 1
    for row in board:
        print('%d|%s' % (row_number,  "|".join(row)) + "|")
        row_number += 1      
    print('------------')

def create_ships(board):
    """
    This function will create 5 ships on random places on the board
    by choosing a random integer between 0 and 4.   
    """
    for ship in range(5):
        ship_column, ship_row = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_column] == "X":
            ship_column, ship_row = randint(0, 4), randint(0, 4)
        board[ship_row][ship_column] = 'X'

def user_guess():
    """
    Take player guess by requesting input on which row and column 
    they want to shoot and will trigger a ValueError if input is not a number  
    """ 
    try:
        row = int(input('Guess between row numbers 1-5: '))
        column = int(input('Guess between column numbers 1-5: '))
    except ValueError:
        print("Invalid answer enter a number between 1-5")
    except TypeError:
        print("Object not supported")
    return int(row) -1, int(column) -1

def hit_ships(board):
    """
    Count hits by going through each row and column looking for X which is a ship on the board 
    and adds 1 if it finds it  
    """
    hits = 0 
    for row in board:
        for column in row:
            if column == 'X':
                hits += 1
    return hits 
"""
Run game will count rounds, subtracting one every new guess, print result of round and print if you win or lose after 
7 rounds.
"""

create_ships(HIDDEN_BOARD)
rounds = 10
while rounds > 0:
    print_board(GUESS_BOARD)
    print('Welcome to Battleships!')
    row,column = user_guess()
    if  HIDDEN_BOARD[row][column]  == "X":
        print('It"s A Hit!')
        print(f'Rounds left, {rounds}')
        rounds -= 1
        GUESS_BOARD[row][column] = "X"
    elif HIDDEN_BOARD[row][column] == "-":
        print('Already tried this one!')
    else:
        print('It"s A Miss!')
        print(f'Rounds left, {rounds}')
        HIDDEN_BOARD[row][column] = '-'
        GUESS_BOARD[row][column] = '*'
        rounds -=1
    if  hit_ships(GUESS_BOARD) == 5:
        print('You won you have sunk all the Battleships')
        break
    if rounds == 0:
        print('Game over! no more guesses')
        break
