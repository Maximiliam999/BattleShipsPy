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
       


def Guess():
    column = input('Guess between column numbers 1-5')
    if column not in '12345':
        print("Invalid answer")
    row = input('Guess between row numbers 1-5')
    if row not in '12345':
        print("Invalid Answer")

def Run_Game():
    HIDDEN_BOARD
    GUESS_BOARD
