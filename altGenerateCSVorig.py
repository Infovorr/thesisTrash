import json
import os

if __name__ == "__main__":
	backdoorList = []
	browsermodList = []
	puaList = []
	pwsList = []
	trojanList = []
	trojandropperList = []
	virtoolList = []
	wormList = []
	trojandownList = []
	uniqueMatrix = []
	vectorMatrix = []
	vectnrMatrix = []
	
	thisFile = open("listBackdoor.txt", "r")
	for item in thisFile:
		backdoorList.append(item)
	thisFile.close()
	thisFile = open("listBrowsermodifier.txt", "r")
	for item in thisFile:
		browsermodList.append(item)
	thisFile.close()
	thisFile = open("listPUA.txt", "r")
	for item in thisFile:
		puaList.append(item)
	thisFile.close()
	thisFile = open("listPWS.txt", "r")
	for item in thisFile:
		pwsList.append(item)
	thisFile.close()
	thisFile = open("listTrojan.txt", "r")
	for item in thisFile:
		trojanList.append(item)
	thisFile.close()
	thisFile = open("listTrojandownloader.txt", "r")
	for item in thisFile:
		trojandownList.append(item)
	thisFile.close()
	thisFile = open("listTrojandropper.txt", "r")
	for item in thisFile:
		trojandropperList.append(item)
	thisFile.close()
	thisFile = open("listVirtool.txt", "r")
	for item in thisFile:
		virtoolList.append(item)
	thisFile.close()
	thisFile = open("listWorm.txt", "r")
	for item in thisFile:
		wormList.append(item)
	thisFile.close()
	
	os.chdir("Unique")
	for i in backdoorList:
		thisRow = "backdoor"
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in browsermodList:
		thisRow = "browserModifier"
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in puaList:
		thisRow = "PUA"
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in pwsList:
		thisRow = "PWS"
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in trojandownList:
		thisRow = "trojanDownloader"
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in trojandropperList:
		thisRow = "trojanDropper"
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in virtoolList:
		thisRow = "virtool"
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in worm:
		thisRow = "worm"
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
		
	os.chdir("..")
	os.chdir("Vector")
	for i in backdoorList:
		thisRow = "backdoor"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		vectorMatrix.append(thisRow)
		
	for i in browsermodList:
		thisRow = "browserModifier"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		vectorMatrix.append(thisRow)
		
	for i in puaList:
		thisRow = "PUA"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		vectorMatrix.append(thisRow)
		
	for i in pwsList:
		thisRow = "PWS"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		vectorMatrix.append(thisRow)
		
	for i in trojandownList:
		thisRow = "trojanDownloader"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		vectorMatrix.append(thisRow)
		
	for i in trojandropperList:
		thisRow = "trojanDropper"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		vectorMatrix.append(thisRow)
		
	for i in virtoolList:
		thisRow = "virtool"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		vectorMatrix.append(thisRow)
		
	for i in wormList:
		thisRow = "worm"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		vectorMatrix.append(thisRow)
		
	os.chdir("..")
	os.chdir("VectorNonRep")
	for i in backdoorList:
		thisRow = "backdoor"
		lastRow = ""
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in browsermodList:
		thisRow = "browserModifier"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in puaList:
		thisRow = "PUA"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in pwsList:
		thisRow = "PWS"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in trojandownList:
		thisRow = "trojanDownloader"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in trojandropperList:
		thisRow = "trojanDropper"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in virtoolList:
		thisRow = "virtool"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in wormList:
		thisRow = "worm"
		counter = 0
		thisFile = open(i[:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	os.chdir("..")
	finalFile1 = open("uniqueOrig.csv", "w")
	for row in uniqueMatrix:
		finalFile1.write(row + "\n")
	finalFile1.close()
	finalFile2 = open("vectorOrig.csv", "w")
	for row in vectorMatrix:
		finalFile2.write(row + "\n")
	finalFile2.close()
	finalFile3 = open("vectnrOrig.csv", "w")
	for row in vectnrMatrix:
		finalFile3.write(row + "\n")
	finalFile3.close()
	
	
	
#load each malware list
#get size of smallest malware list
#iterate through each malware list, up to the length of the smallest list
#	open unique file
#		write elements to list, skipping blanks
#	open vector file
#		write 50 elements to list, skipping blanks
#	open vectnr file
#		write 50 elements to list, skipping blanks and consecutive reps
#	append each list to appropriate matrix
#write each matrix to text