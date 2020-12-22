if __name__ == "__main__":
	row = ["backdoor", "x14", "x55", "x28", "x36", "x27", "x15", "x16", "x47", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]
	thisRow = [row[0]]
	#print(thisRow)
	thisElement = 0
	for column in row:
		workRow = []
		#print(workRow)
		if thisElement != 0:
			workRow = ["0"] * 71
			if column != "NA":
				workRow[int(column[1:])] = "1"
				#print(int(column[1:]))
				#print(workRow[int(column[1:])])
		thisElement += 1
		thisRow += workRow
	#print(thisRow)
	#print(len(row))
	#print(len(thisRow))
	if len(thisRow) != 3551:
		leftover = 3551 - len(thisRow)
		if leftover < 0:
			print(leftover)
		thisRow += ["0"] * leftover
	print(thisRow)