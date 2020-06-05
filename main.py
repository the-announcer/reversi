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
			print(col + " {}".format(" "), end='')
		
		print('\n')



## main stuff

b = createBoard()
printBoard(b)





	

