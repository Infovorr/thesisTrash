import json
import os

if __name__ == "__main__":
	apiFile1 = open("api.json", "r")
	apiDict1 = json.load(apiFile1)
	apiFile1.close()
	apiDict2 = {}
	os.chdir("VectorNonRep")
	fileList = os.listdir()
	for i in fileList:
		thisFile = open(i, "r")
		for line in thisFile:
			if "***URL" in line or "***Diagnosis" in line:
				break
			if "***" not in line:
				if line[:-1] in apiDict2:
					apiDict2[line[:-1]] = apiDict2[line[:-1]] + 1
				else:
					apiDict2[line[:-1]] = 0
		thisFile.close()
	list1 = list(apiDict1.keys())
	list2 = list(apiDict2.keys())
	list3 = []
	for i in list2:
		if i not in list1:
			list3.append(i)
	finalFile = open("wrongAPIs.json", "w")
	for i in list3:
		finalFile.write(i + "\n")
	finalFile.close()