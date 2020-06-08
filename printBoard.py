def printBoard(b):
	
	width = range(len(b[0]))

	print("  ", end="")
	for n in width:
		x_ascii = n+65 	# capital A is 65

		if n < max(width):
			# print(str(n+1) + " ", end="")
			print(chr(x_ascii) + " " , end="")
		else:
			# print(str(n+1))
			print(chr(x_ascii))
	

	for i in range(len(b)):
		col = b[i]

		# x_ascii = i+65 	# capital A is 65
		# print(chr(x_ascii) + " " , end="")
		print(str(i+1) + " ", end="")

		for j in range(len(col)):
			row = col[j]
			
			if j < (len(col)-1):
				print(row + "{}".format(" "), end="")
			else:
				print(row + "{}".format(" "))

				#

