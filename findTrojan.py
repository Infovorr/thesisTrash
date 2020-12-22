import os

if __name__ == "__main__":
	os.chdir("Unique")
	fileList = os.listdir()
	trojanList = []
	for item in fileList:
		currentFile = open(item, "r")
		for line in currentFile:
			if "***Diagnosis" in line:
				currentFile.readline()
				thisline = currentFile.readline()
				print(thisline[:-1])
				if thisline[:-1] == "Trojan":
					trojanList.append(item)
		currentFile.close()
	os.chdir("..")
	trojanFile = open("trojanList.txt", "w")
	for item in trojanList:
		trojanFile.write(item + "\n")
	trojanFile.close()