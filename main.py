from createBoard import createBoard
from printBoard import printBoard
from getMove import getMove
from putMarker import putMarker
from flipColors import flipColors
from translateDirection import translateDirection

######################
## REVERSI GAME
######################


# make a new board
b = createBoard()


# print the board
printBoard(b)


# ask user for their move
marker = getMove()
putMarker(marker, b)

search_direction = 'nw'
flipColors(marker, b, search_direction)
