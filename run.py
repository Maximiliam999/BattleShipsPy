from random import randint

HIDDEN_BOARD = [[' '] * 5 for x in range(5)]
GUESS_BOARD = [[' '] * 5 for x in range(5)]


def print_board(board):
    row_number = 1
    for row in board:
        print('%d|%s' % (row_number, "|".join(row)))
        row_number += 1      



def create_ships(board):
    for ship in range(4):
        ship_column, ship_row = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_column] == "X":
            ship_column, ship_row = randint(0, 4), randint(0, 4)
        board[ship_row][ship_column] = 'X'
        


def User_guess():
    try:
        column = input('Guess between column numbers 1-5: ')
        row = input('Guess between row numbers 1-5: ')
    except ValueError:
        print("Invalid answer enter a number between 1-5")
    return int(row) -1, int(column) -1


def hit_ships(board):
    hits = 0 
    for row in board:
        for column in row:
            if column == 'X':
                hits += 1
    return hits 
    
print_board(GUESS_BOARD)
#print_board(HIDDEN_BOARD)

##def Run_Game():

rounds = 0
while rounds < 8:
    print('Welcome to Battleships!')
    row,column = User_guess()
    if [row][column]  == "X":
        print('It"s A Hit!')
        rounds += 1
    elif [row][column] != "-":
        print('Already tried this one!')
    else:
        print('It"s A Miss!') 


create_ships(board)
create_ships(HIDDEN_BOARD)


    

