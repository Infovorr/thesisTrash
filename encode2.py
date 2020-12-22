import json
import os

if __name__ == "__main__":
	EORfile = []
	EC1file = []
	EC2file = []
	NORfile = []
	NC1file = []
	NC2file = []
	
	apiOrig = {}
	apiCom1 = {}
	apiCom2 = {}
	
	EORout = []
	EC1out = []
	EC2out = []
	NORout = []
	NC1out = []
	NC2out = []
	
	thisRow = []
	
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
	
	for row in EORfile:
		thisRow = [row[0]]
		thisElement = 0
		for column in row:
			workRow = []
			if thisElement != 0:
				workRow = ["0"] * 663
				if column != "NA":
					workRow[apiOrig[column]] = "1"
			thisElement += 1
			thisRow += workRow
		if len(thisRow) != 33151:
			leftover = 33151 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		EORout.append(thisRow)
		
	for row in NORfile:
		thisRow = [row[0]]
		thisElement = 0
		for column in row:
			workRow = []
			if thisElement != 0:
				workRow = ["0"] * 663
				if column != "NA":
					workRow[apiOrig[column]] = "1"
			thisElement += 1
			thisRow += workRow
		if len(thisRow) != 33151:
			leftover = 33151 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		NORout.append(thisRow)
	
	for row in EC1file:
		thisRow = [row[0]]
		thisElement = 0
		for column in row:
			workRow = []
			if thisElement != 0:
				workRow = ["0"] * 71
				if column != "NA":
					workRow[int(column[1:])] = "1"
			thisElement += 1
			thisRow += workRow
		if len(thisRow) != 3551:
			leftover = 3551 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		EC1out.append(thisRow)
		
	for row in NC1file:
		thisRow = [row[0]]
		thisElement = 0
		for column in row:
			workRow = []
			if thisElement != 0:
				workRow = ["0"] * 71
				if column != "NA":
					workRow[int(column[1:])] = "1"
			thisElement += 1
			thisRow += workRow
		if len(thisRow) != 3551:
			leftover = 3551 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		NC1out.append(thisRow)
	
	for row in EC2file:
		thisRow = [row[0]]
		thisElement = 0
		for column in row:
			workRow = []
			if thisElement != 0:
				workRow = ["0"] * 41
				if column != "NA":
					workRow[int(column[1:])] = "1"
			thisElement += 1
			thisRow += workRow
		if len(thisRow) != 2051:
			leftover = 2051 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		EC2out.append(thisRow)
		
	for row in NC2file:
		thisRow = [row[0]]
		thisElement = 0
		for column in row:
			workRow = []
			if thisElement != 0:
				workRow = ["0"] * 41
				if column != "NA":
					workRow[int(column[1:])] = "1"
			thisElement += 1
			thisRow += workRow
		if len(thisRow) != 2051:
			leftover = 2051 - len(thisRow)
			if leftover < 0:
				print(leftover)
			thisRow += ["0"] * leftover
		NC2out.append(thisRow)
		
	os.chdir("encodedFiles")
	
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