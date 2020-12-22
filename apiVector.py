import os

if __name__ == "__main__":
	apiAll = []
	apiList = []
	apiListU = []
	apiNew = []
	apiLast = []
	fileHash = ""
	os.chdir("apiLog")
	fileList = os.listdir()
	totalFiles = len(fileList) - 1
	currentFile = 11
	oldHash = open(fileList[11], "r", encoding = "latin-1")
	for line in oldHash:
		if "### SAMPLE #" in line:
			fileHash = line[(line.index(" - ") + 3):-1]
			break
	while currentFile < totalFiles:
		print("Reading file " + fileList[currentFile])
		for line in oldHash:
			if "API::" in line:
				apiNew = line[(line.index("API::") + 5):]
				if " " in apiNew:
					apiNew = apiNew[:(apiNew.index(" "))]
				if ":" in apiNew:
					apiNew = apiNew[:(apiNew.index(":"))]
				if "(" in apiNew:
					apiNew = apiNew[:(apiNew.index("("))]
				if ")" in apiNew:
					apiNew = ""
				if "," in apiNew:
					apiNew = ""
				if len(apiNew) != 0:
					apiList.append(apiNew)
					if apiNew != apiLast:
						apiListU.append(apiNew)
					apiLast = apiNew
					if apiNew not in apiAll:
						apiAll.append(apiNew)
			if "### SAMPLE #" in line:
				newFile = open(".\\eVectorSamples\\" + fileHash, "w")
				newFile.write("***API***\n")
				for item in apiList:
					newFile.write(item + "\n")
				newFile.write("***Diagnosis***\n")
				newFile.close()
				newFile2 = open(".\\eVectorSamplesU\\" + fileHash, "w")
				newFile2.write("***API***\n")
				for item in apiListU:
					newFile2.write(item + "\n")
				newFile2.write("***Diagnosis***\n")
				newFile2.close()
				apiList.clear()
				apiListU.clear()
				apiLast = ""
				fileHash = line[(line.index(" - ") + 3):-1]
		oldHash.close()
		currentFile += 1
		if currentFile >= totalFiles:
			break
		oldHash = open(fileList[currentFile], "r", encoding = "latin-1")
	apiOutput = open("apiTotal2.txt", "w")
	for item in apiAll:
		apiOutput.write(item + "\n")
	apiOutput.close()