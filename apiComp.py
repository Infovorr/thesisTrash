import json
import os

if __name__ == "__main__":
	apiDictFile = open("api.json", "r")
	apiComp = json.load(apiDictFile)
	apiDictFile.close()
	apiList = list(apiComp.keys())
	apiOrig = {}
	apiPos = 0
	for i in apiList:
		apiOrig[i] = apiPos
		apiPos += 1
	filePos = 0
	apiCompFileA = open("apiCompilation.txt", "r")
	for line in apiCompFileA:
		currentList = line.split(";")
		if currentList[-1].endswith("\n"):
			currentList[-1] = currentList[-1][:-1]
		for item in currentList:
			apiComp[item] = filePos
		filePos += 1
	apiCompFileA.close()
	apiOrigFile = open("apiOrig.json", "w")
	json.dump(apiOrig, apiOrigFile, indent = 4)
	apiOrigFile.close()
	apiCompFile = open("apiComp.json", "w")
	json.dump(apiComp, apiCompFile, indent = 4)
	apiCompFile.close()