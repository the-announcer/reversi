from createBoard import createBoard
from printBoard import printBoard
from getMove import getMove
from putMarker import putMarker
from flipColors import flipColors
from inspectBoard import inspectBoard

######################
## REVERSI GAME
######################


# make a new board
b = createBoard()


# print the board
printBoard(b)

p1 = 'X'
p2 = 'O'

# ask user for their move
marker = getMove(p1)
b = putMarker(marker, b, p1)

heading = 4 # this is default current position of marker

pieces = []
b = inspectBoard(marker, b, heading, pieces)

printBoard(b)