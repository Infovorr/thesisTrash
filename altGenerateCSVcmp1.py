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
	
	dictFile = open("apiComp.json", "r")
	apiDict = json.load(dictFile)
	dictFile.close()
	
	sizeList.append(len(backdoorList))
	sizeList.append(len(browsermodList))
	sizeList.append(len(puaList))
	sizeList.append(len(pwsList))
	sizeList.append(len(softbundList))
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
		thisRow = "backdoor"
		elems = []
		thisFile = open(backdoorList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "browserModifier"
		elems = []
		thisFile = open(browsermodList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
				counter += 1
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "PUA"
		elems = []
		thisFile = open(puaList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "PWS"
		elems = []
		thisFile = open(pwsList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "softwareBundler"
		elems = []
		thisFile = open(softbundList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
				counter += 1
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojanDownloader"
		elems = []
		thisFile = open(trojandownList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojanDropper"
		elems = []
		thisFile = open(trojandropperList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "virtool"
		elems = []
		thisFile = open(virtoolList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
		uniqueMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "worm"
		elems = []
		thisFile = open(wormList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and apiDict[j[:-1]] not in elems:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				elems.append(apiDict[j[:-1]])
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
				thisRow += "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
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
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "browserModifier"
		counter = 0
		thisFile = open(browsermodList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "PUA"
		counter = 0
		thisFile = open(puaList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "PWS"
		counter = 0
		thisFile = open(pwsList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "softwareBundler"
		counter = 0
		thisFile = open(softbundList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojanDownloader"
		counter = 0
		thisFile = open(trojandownList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "trojanDropper"
		counter = 0
		thisFile = open(trojandropperList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "virtool"
		counter = 0
		thisFile = open(virtoolList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	for i in range(sampleSize):
		thisRow = "worm"
		counter = 0
		thisFile = open(wormList[i][:-1], "r")
		for j in thisFile:
			if "***URL" in j or counter >= 50 or "***Diag" in j:
				break
			if j[:-1] != "" and "***" not in j and ("x" + str(apiDict[j[:-1]])) != lastRow:
				thisRow += ","
				thisRow += "x" + str(apiDict[j[:-1]])
				lastRow = "x" + str(apiDict[j[:-1]])
				counter += 1
		thisFile.close()
		vectnrMatrix.append(thisRow)
		
	os.chdir("..")
	finalFile1 = open("uniqueCmp1.csv", "w")
	for row in uniqueMatrix:
		finalFile1.write(row + "\n")
	finalFile1.close()
	finalFile2 = open("vectorCmp1.csv", "w")
	for row in vectorMatrix:
		finalFile2.write(row + "\n")
	finalFile2.close()
	finalFile3 = open("vectnrCmp1.csv", "w")
	for row in vectnrMatrix:
		finalFile3.write(row + "\n")
	finalFile3.close()
	
	
	
#load each malware list
#get size of smallest malware list
#iterate through each malware list, up to the length of the smallest list
#	open unique file
#		get elements, skipping blanks
#		write corresponding integer from appropriate api dict to list
#	open vector file
#		get 50 elements, skipping blanks
#		write corresponding integer from appropriate api dict to list
#	open vectnr file
#		get 50 elements, skipping blanks and consecutive reps
#		write corresponding integer from appropriate api dict to list
#	append each list to appropriate matrix
#write each matrix to text