from random import randint 

scores = {"computer": 0, "player":0}

class Board:
    """
    Board class, sets board size and number of ships.
    """
    def __init__(self, size,num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.name = name
        self.num_ships = num_ships
        self.type = type
        self.guesses = []
        self.ship = []

    def print(self):
        for row in self.board:
            print("".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if(x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ships(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add any more ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"