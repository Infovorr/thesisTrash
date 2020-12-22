import os

if __name__ == "__main__":
	apiAll = []
	apiList = []
	apiNew = []
	urlList = []
	fileHash = ""
	fileList = os.listdir()
	totalFiles = len(fileList) - 1
	currentFile = 3
	oldHash = open(fileList[3], "r", encoding = "latin-1")
	#print("Reading file " + fileList[2])
	for line in oldHash:
		if "### SAMPLE #" in line:
			fileHash = line[(line.index(" - ") + 3):-1]
			break
	while currentFile < totalFiles:
		print("Reading file " + fileList[currentFile])
		for line in oldHash:
			if "API::" in line:
				apiNew = line[(line.index("API::") + 5):]
				#print(apiNew)
				if " " in apiNew:
					apiNew = apiNew[:(apiNew.index(" "))]
				if apiNew not in apiList:
					apiList.append(apiNew)
				if apiNew not in apiAll:
					apiAll.append(apiNew)
					#print(apiNew)
			if "=http" in line:
				urlList.append(line)
			if "### SAMPLE #" in line:
				newFile = open(".\\newSamples\\" + fileHash, "w")
				newFile.write("***API***\n")
				for item in apiList:
					newFile.write(item + "\n")
				newFile.write("***URL***\n")
				for item in urlList:
					newFile.write(item + "\n")
				newFile.write("***Diagnosis***\n")
				newFile.close()
				apiList.clear()
				urlList.clear()
				fileHash = line[(line.index(" - ") + 3):-1]
		oldHash.close()
		currentFile += 1
		if currentFile >= totalFiles:
			break
		oldHash = open(fileList[currentFile], "r", encoding = "latin-1")
		#print("Reading file " + fileList[currentFile])
	apiOutput = open(".\\newSamples\\apiTotal.txt", "w")
	for item in apiAll:
		apiOutput.write(item + "\n")
	apiOutput.close()