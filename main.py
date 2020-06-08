from createBoard import createBoard
from createBoard import createBoardSpecial
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
# b = createBoardSpecial()

# print the board
printBoard(b)

p1 = 'X'
p2 = 'O'
heading = None # this is default current position of marker
pieces = []

while True:

    move = getMove(p1)
    b = putMarker(move, b, p1)
    b = inspectBoard(move, b, heading, pieces)
    printBoard(b)

    move = getMove(p2)
    b = putMarker(move, b, p2)
    b = inspectBoard(move, b, heading, pieces)
    printBoard(b)
