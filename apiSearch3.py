import json
import os

if __name__ == "__main__":
	apiDict = {}
	os.chdir("VectorNonRep")
	fileList = os.listdir()
	for i in fileList:
		print("Reading " + i)
		thisFile = open(i, "r")
		for line in thisFile:
			if "***URL" in line or "***Diagnosis" in line:
				break
			if "***" not in line:
				if line[:-1] in apiDict:
					apiDict[line[:-1]] = apiDict[line[:-1]] + 1
				else:
					apiDict[line[:-1]] = 1
		thisFile.close()
	os.chdir("..")
	list1 = list(apiDict.keys())
	finalFile = open("wrongAPIs.json", "w")
	json.dump(apiDict, finalFile, indent = 4)
	finalFile.close()