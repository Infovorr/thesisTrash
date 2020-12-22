import os

if __name__ == "__main__":
	os.chdir("C:\\apiFiles\\Unique")
	fileList = os.listdir()
	diagFlag = False
	position = 0
	backdoorList = []
	trojanList = []
	puaList = []
	for item in fileList:
		print("Searching " + item)
		currentFile = open(item, "r")
		for line in currentFile:
			if diagFlag:
				if position == 1:
					if line == "Backdoor\n":
						print(line)
						backdoorList.append(item)
						break
					elif line == "Trojan\n":
						print(line)
						trojanList.append(item)
						break
					elif line == "PUA\n":
						print(line)
						puaList.append(item)
						break
					else:
						break
				else:
					position += 1
			if line == "***Diagnosis***\n":
				diagFlag = True
		diagFlag = False
		position = 0
		currentFile.close()
	os.chdir("..")
	backdoorFile = open("backdoor.txt", "w")
	for backdoor in backdoorList:
		backdoorFile.write(backdoor + "\n")
	backdoorFile.close()
	trojanFile = open("trojan.txt", "w")
	for trojan in trojanList:
		trojanFile.write(trojan + "\n")
	trojanFile.close()
	puaFile = open("pua.txt", "w")
	for pua in puaList:
		puaFile.write(pua + "\n")
	puaFile.close()