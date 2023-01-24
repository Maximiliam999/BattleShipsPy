from random import randint 

board = []

for x in range(5):
    board.append(['*'] * 5)

def print_board(board):
    for row in board:
        print((' ').join(row))