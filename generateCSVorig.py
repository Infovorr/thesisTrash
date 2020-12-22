import json
import os

if __name__ == "__main__":
	backdoorList = []
	browsermodList = []
	puaList = []
	pwsList = []
	softbundList = []
	trojanList = []
	trojandropperList = []
	virtoolList = []
	wormList = []
	trojandownList = []
	uniqueMatrix = []
	vectorMatrix = []
	vectnrMatrix = []
	sizeList = []
	apiDict = {}
	
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
	thisFile = open("listSoftwarebundler.txt", "r")
	for item in thisFile:
		softbundList.append(item)
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
	thisFile = open("apisOrd.json", "r")
	apiDict = json.load(thisFile)
	thisFile.close()
	
	sizeList.append(len(backdoorList))
	sizeList.append(len(browsermodList))
	sizeList.append(len(puaList))
	sizeList.append(len(pwsList))
	sizeList.append(len(softbundList))
	sizeList.append(len(trojanList))
	sizeList.append(len(trojandownList))
	sizeList.append(len(trojandropperList))
	sizeList.append(len(virtoolList))
	sizeList.append(len(wormList))
	sizeList.sort()
	#print(sizeList)
	sampleSize = sizeList[0]
	print(sampleSize)
	
	os.chdir("Unique")
	for i in range(sampleSize):
		thisRow = ["backdoor"]
		thisRowA = ["0"] * 663
		thisFile = open(backdoorList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["browserModifier"]
		thisRowA = ["0"] * 663
		thisFile = open(browsermodList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["PUA"]
		thisRowA = ["0"] * 663
		thisFile = open(puaList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["PWS"]
		thisRowA = ["0"] * 663
		thisFile = open(pwsList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["softwareBundler"]
		thisRowA = ["0"] * 663
		thisFile = open(softbundList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["trojan"]
		thisRowA = ["0"] * 663
		thisFile = open(softbundList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["trojanDownloader"]
		thisRowA = ["0"] * 663
		thisFile = open(trojandownList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["trojanDropper"]
		thisRowA = ["0"] * 663
		thisFile = open(trojandropperList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["virtool"]
		thisRowA = ["0"] * 663
		thisFile = open(virtoolList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = ["worm"]
		thisRowA = ["0"] * 663
		thisFile = open(wormList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRowA[apiDict[j[:-1]]] = "1"
		thisFile.close()
		thisRow += thisRowA
		uniqueMatrix.append(thisRow)
		
		
		
	os.chdir("..")
	os.chdir("Vector")
	for i in range(sampleSize):
		thisRow = "backdoor"
		counter = 0
		thisFile = open(backdoorList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "browserModifier"
		counter = 0
		thisFile = open(browsermodList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "PUA"
		counter = 0
		thisFile = open(puaList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "PWS"
		counter = 0
		thisFile = open(pwsList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "softwareBundler"
		counter = 0
		thisFile = open(softbundList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojan"
		counter = 0
		thisFile = open(softbundList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojanDownloader"
		counter = 0
		thisFile = open(trojandownList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojanDropper"
		counter = 0
		thisFile = open(trojandropperList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "virtool"
		counter = 0
		thisFile = open(virtoolList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "worm"
		counter = 0
		thisFile = open(wormList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j:
				thisRow += ","
				thisRow += j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectorMatrix.append(thisRow)
		
		
		
	os.chdir("..")
	os.chdir("VectorNonRep")
	for i in range(sampleSize):
		thisRow = "backdoor"
		lastRow = ""
		counter = 0
		thisFile = open(backdoorList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "browserModifier"
		counter = 0
		thisFile = open(browsermodList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "PUA"
		counter = 0
		thisFile = open(puaList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "PWS"
		counter = 0
		thisFile = open(pwsList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "softwareBundler"
		counter = 0
		thisFile = open(softbundList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojan"
		counter = 0
		thisFile = open(trojandownList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojanDownloader"
		counter = 0
		thisFile = open(trojandownList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojanDropper"
		counter = 0
		thisFile = open(trojandropperList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "virtool"
		counter = 0
		thisFile = open(virtoolList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "worm"
		counter = 0
		thisFile = open(wormList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and j[:-1] != lastRow:
				thisRow += ","
				thisRow += j[:-1]
				lastRow = j[:-1]
				counter += 1
		thisFile.close()
		if counter < 50:
			thisRow += ",NA" * (50 - counter)
		vectnrMatrix.append(thisRow)
		
	os.chdir("..")
	finalFile1 = open("uniqueOrig.csv", "w")
	for row in uniqueMatrix:
		thisString = ""
		for cell in row:
			thisString += cell + ","
		thisString = thisString[:-1] + "\n"
		finalFile1.write(thisString)
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