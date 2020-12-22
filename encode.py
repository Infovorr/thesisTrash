import json
import os

if __name__ == "__main__":
	UORfile = []
	UC1file = []
	UC2file = []
	EORfile = []
	EC1file = []
	EC2file = []
	NORfile = []
	NC1file = []
	NC2file = []
	
	apiOrig = {}
	apiCom1 = {}
	apiCom2 = {}
	
	UORout = []
	UC1out = []
	UC2out = []
	EORout = []
	EC1out = []
	EC2out = []
	NORout = []
	NC1out = []
	NC2out = []
	
	thisRow = []
	
	thisFile = open("uniqueOrig.csv", "r")
	for line in thisFile:
		UORfile.append(line[:-1].split(","))
	thisFile.close()
	thisFile = open("uniqueCmp1.csv", "r")
	for line in thisFile:
		UC1file.append(line[:-1].split(","))
	thisFile.close()
	thisFile = open("uniqueCmp2.csv", "r")
	for line in thisFile:
		UC2file.append(line[:-1].split(","))
	thisFile.close()
	thisFile = open("vectorOrig.csv", "r")
	for line in thisFile:
		EORfile.append(line[:-1].split(","))
	thisFile.close()
	thisFile = open("vectorCmp1.csv", "r")
	for line in thisFile:
		EC1file.append(line[:-1].split(","))
	thisFile.close()
	thisFile = open("vectorCmp2.csv", "r")
	for line in thisFile:
		EC2file.append(line[:-1].split(","))
	thisFile.close()
	thisFile = open("vectnrOrig.csv", "r")
	for line in thisFile:
		NORfile.append(line[:-1].split(","))
	thisFile.close()
	thisFile = open("vectnrCmp1.csv", "r")
	for line in thisFile:
		NC1file.append(line[:-1].split(","))
	thisFile.close()
	thisFile = open("vectnrCmp2.csv", "r")
	for line in thisFile:
		NC2file.append(line[:-1].split(","))
	thisFile.close()
	
	thisFile = open("apisOrd.json", "r")
	apiOrig = json.load(thisFile)
	thisFile.close()
	thisFile = open("apiComp.json", "r")
	apiCom1 = json.load(thisFile)
	thisFile.close()
	thisFile = open("apiComp2.json", "r")
	apiCom2 = json.load(thisFile)
	thisFile.close()
	
	for row in UORfile:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		workRow = ["0"] * 663
		for column in row:
			if thisElement != 0:
				workRow[apiOrig[column]] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 88189:
			leftover = 88189 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		UORout.append(thisRow)
	
	for row in EORfile:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		for column in row:
			workRow = ["0"] * 663
			if thisElement != 0:
				workRow[apiOrig[column]] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 33160:
			leftover = 33160 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		EORout.append(thisRow)
		
	for row in NORfile:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		for column in row:
			workRow = ["0"] * 663
			if thisElement != 0:
				workRow[apiOrig[column]] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 33160:
			leftover = 33160 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		NORout.append(thisRow)
		

	for row in UC1file:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		workRow = ["0"] * 71
		for column in row:
			if thisElement != 0:
				workRow[int(column[1:])] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 9453:
			leftover = 9453 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		UC1out.append(thisRow)
	
	for row in EC1file:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		for column in row:
			workRow = ["0"] * 71
			if thisElement != 0:
				workRow[int(column[1:])] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 3560:
			leftover = 3560 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		EC1out.append(thisRow)
		
	for row in NC1file:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		for column in row:
			workRow = ["0"] * 71
			if thisElement != 0:
				workRow[int(column[1:])] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 3560:
			leftover = 3560 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		NC1out.append(thisRow)
		
	
	for row in UC2file:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		workRow = ["0"] * 41
		for column in row:
			if thisElement != 0:
				workRow[int(column[1:])] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 5463:
			leftover = 5463 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		UC2out.append(thisRow)
	
	for row in EC2file:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		for column in row:
			workRow = ["0"] * 41
			if thisElement != 0:
				workRow[int(column[1:])] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 2060:
			leftover = 2060 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		EC2out.append(thisRow)
		
	for row in NC2file:
		thisRow = []
		thisElement = 0
		workRow = ["0"] * 10
		if row[0] == "backdoor":
			workRow[0] = "1"
		elif row[0] == "browserModifier":
			workRow[1] = "1"
		elif row[0] == "PUA":
			workRow[2] = "1"
		elif row[0] == "PWS":
			workRow[3] = "1"
		elif row[0] == "softwareBundler":
			workRow[4] = "1"
		elif row[0] == "trojan":
			workRow[5] = "1"
		elif row[0] == "trojanDownloader":
			workRow[6] = "1"
		elif row[0] == "trojanDropper":
			workRow[7] = "1"
		elif row[0] == "virtool":
			workRow[8] = "1"
		elif row[0] == "worm":
			workRow[9] = "1"
		thisRow += workRow
		for column in row:
			workRow = ["0"] * 41
			if thisElement != 0:
				workRow[int(column[1:])] = "1"
			thisElement += 1
		thisRow += workRow
		if len(thisRow) != 2060:
			leftover = 2060 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		NC2out.append(thisRow)
		
	os.chdir("encodedFiles")
	
	newFile = open("eUniqueOrig.csv", "w")
	for row in UORout:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()
	
	newFile = open("eUniqueCmp1.csv", "w")
	for row in UC1out:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()
	
	newFile = open("eUniqueCmp2.csv", "w")
	for row in UC2out:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()
	
	newFile = open("eVectorOrig.csv", "w")
	for row in EORout:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()
	
	newFile = open("eVectorCmp1.csv", "w")
	for row in EC1out:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()
	
	newFile = open("eVectorCmp2.csv", "w")
	for row in EC2out:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()
	
	newFile = open("eVectnrOrig.csv", "w")
	for row in NORout:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()
	
	newFile = open("eVectnrCmp1.csv", "w")
	for row in NC1out:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()
	
	newFile = open("eVectnrCmp2.csv", "w")
	for row in NC2out:
		outString = ""
		for cell in row:
			outString += cell
			outString += ","
		outString = outString[:-1]
		newFile.write(outString + "\n")
	newFile.close()