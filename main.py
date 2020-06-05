## REVERSI GAME

def createBoard():
	board = [
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','X','O','-','-','-',],
		['-','-','-','O','X','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',],
		['-','-','-','-','-','-','-','-',]
	]
	
	return board

def printBoard(b):
	
	width = range(len(b[0]))

	print("  ", end="")
	for n in width:
		if n < max(width):
			print(str(n+1) + " ", end="")
		else:
			print(str(n+1))
	

	for i in range(len(b)):
		row = b[i]

		y_ascii = i+65 	# capital A is 65
		print(chr(y_ascii) + " " , end="")

		for j in range(len(row)):
			col = row[j]			
			
			if j < (len(row)-1):
				print(col + "{}".format(" "), end="")
			else:
				print(col + "{}".format(" "))


## main stuff

b = createBoard()
printBoard(b)





	

