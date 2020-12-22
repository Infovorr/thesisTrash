import os

if __name__ == "__main__":
	os.chdir("Unique")
	fileList = os.listdir()
	trojandownloaderList = []
	for item in fileList:
		currentFile = open(item, "r")
		for line in currentFile:
			if "***Diagnosis" in line:
				currentFile.readline()
				thisline = currentFile.readline()
				print(thisline[:-1])
				if thisline[:-1] == "TrojanDownloader":
					trojandownloaderList.append(item)
		currentFile.close()
	os.chdir("..")
	trojandownloaderFile = open("trojandownloaderList.txt", "w")
	for item in trojandownloaderList:
		trojandownloaderFile.write(item + "\n")
	trojandownloaderFile.close()