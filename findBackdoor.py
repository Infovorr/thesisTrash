import os

if __name__ == "__main__":
	os.chdir("Unique")
	fileList = os.listdir()
	backdoorList = []
	for item in fileList:
		currentFile = open(item, "r")
		for line in currentFile:
			if "***Diagnosis" in line:
				currentFile.readline()
				thisline = currentFile.readline()
				print(thisline[:-1])
				if thisline[:-1] == "Backdoor":
					backdoorList.append(item)
		currentFile.close()
	os.chdir("..")
	backdoorFile = open("backdoorList.txt", "w")
	for item in backdoorList:
		backdoorFile.write(item + "\n")
	backdoorFile.close()