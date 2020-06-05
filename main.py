## REVERSI GAME

def createBoard():
	board = [
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',]
	]
	
	return board

def printBoard(b):
	
	for i in range(len(b)):
		row = b[i]

		for j in range(len(row)):
			col = row[j]			
			
			if j < (len(row)-1):
				print(col + "{}".format(" "), end="")
			else:
				print(col + "{}".format(" "))


## main stuff

b = createBoard()
printBoard(b)





	

