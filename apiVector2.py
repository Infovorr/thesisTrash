import os

if __name__ == "__main__":
	apiList = []
	apiNew = []
	fileHash = ""
	os.chdir(".\\apiLog")
	fileList = os.listdir()
	totalFiles = len(fileList) - 1
	currentFile = 10
	oldHash = open(fileList[10], "r", encoding = "latin-1")
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
				if len(apiNew != 0):
					apiList.append(apiNew)
			if "### SAMPLE #" in line:
				newFile = open(".\\vectorSamples\\" + fileHash, "w")
				newFile.write("***API***\n")
				for item in apiList:
					newFile.write(item + "\n")
				newFile.write("***Diagnosis***\n")
				newFile.close()
				apiList.clear()
				fileHash = line[(line.index(" - ") + 3):-1]
		oldHash.close()
		currentFile += 1
		if currentFile >= totalFiles:
			break
		oldHash = open(fileList[currentFile], "r", encoding = "latin-1")