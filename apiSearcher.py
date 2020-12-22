import json
import os

if __name__ == "__main__":
	os.chdir("Unique")
	fileList = os.listdir()
	apiDict = {}
	ordinal = 0
	for i in fileList:
		thisFile = open(i, "r")
		for line in thisFile:
			if "***URL" in line or "***Diagnosis" in line:
				break
			if "***" not in line and len(line[:-1]) != 0:
				if line[:-1] not in apiDict:
					apiDict[line[:-1]] = ordinal
					ordinal += 1
		thisFile.close()
	os.chdir("..")
	finalFile = open("apisOrd.json", "w")
	json.dump(apiDict, finalFile, indent = 4)
	finalFile.close()