from createBoard import createBoard
from printBoard import printBoard
from getMove import getMove

######################
## REVERSI GAME
######################


# make a new board
b = createBoard()


# print the board
printBoard(b)


# ask user for their move
player_p1 = getMove()
# print(player_p1)