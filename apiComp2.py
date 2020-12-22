import json
import os

if __name__ == "__main__":
	apiDictFile = open("api.json", "r")
	#apiComp = json.load(apiDictFile)
	apiComp2 = json.load(apiDictFile)
	apiDictFile.close()
	apiList = list(apiComp2.keys())
	apiOrig = {}
	apiPos = 0
	for i in apiList:
		apiOrig[i] = apiPos
		apiPos += 1
	filePos = 0
	#apiCompFileA = open("apiCompilation.txt", "r")
	#for line in apiCompFileA:
	#	currentList = line.split(";")
	#	if currentList[-1].endswith("\n"):
	#		currentList[-1] = currentList[-1][:-1]
	#	for item in currentList:
	#		apiComp[item] = filePos
	#	filePos += 1
	#apiCompFileA.close()
	apiCompFileB = open("apiComp2.txt", "r")
	for line in apiCompFileB:
		currentList = line.split(";")
		if currentList[-1].endswith("\n"):
			currentList[-1] = currentList[-1][:-1]
		for item in currentList:
			apiComp2[item] = filePos
		filePos += 1
	apiCompFileB.close()
	#apiOrigFile = open("apiOrig.json", "w")
	#json.dump(apiOrig, apiOrigFile, indent = 4)
	#apiOrigFile.close()
	#apiCompFile = open("apiComp.json", "w")
	#json.dump(apiComp, apiCompFile, indent = 4)
	#apiCompFile.close()
	apiCompFile2 = open("apiComp2.json", "w")
	json.dump(apiComp2, apiCompFile2, indent = 4)
	apiCompFile2.close()