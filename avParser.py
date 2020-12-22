import json
import os

if __name__ == "__main__":
	avList = {}
	avclassList = {}
	msclassList = {}
	saclassList = {}
	apiList = {}
	os.chdir(".\\evenNewer\\jason")
	fileList = os.listdir()
	avList["TOTAL"] = len(fileList)
	total = 0
	for item in fileList:
		currentFile = open(item, "r", encoding = "latin-1")
		print("Reading " + item)
		avDump = json.load(currentFile)
		thisClass = ""
		if "scans" in avDump:
			avDump = avDump["scans"]
			if "Avast" in avDump:
				classDump = avDump["Avast"]
				if classDump["detected"]:
					total += 1
					thisClass = classDump["result"]
					if "[" in thisClass:
						thisClass = thisClass[(thisClass.index("[") + 1):(thisClass.index("]"))]
						if thisClass in avclassList:
							avclassList[thisClass] = avclassList[thisClass] + 1
						else:
							avclassList[thisClass] = 1
			if "Microsoft" in avDump:
				classDump = avDump["Microsoft"]
				if classDump["detected"]:
					total += 1
					thisClass = classDump["result"]
					if ":" in thisClass:
						thisClass = thisClass[:thisClass.index(":")]
						if thisClass in msclassList:
							msclassList[thisClass] = msclassList[thisClass] + 1
						else:
							msclassList[thisClass] = 1
			if "SUPERAntiSpyware" in avDump:
				classDump = avDump["SUPERAntiSpyware"]
				if classDump["detected"]:
					total += 1
					thisClass = classDump["result"]
					if "." in thisClass:
						thisClass = thisClass[:thisClass.index(".")]
						if thisClass in saclassList:
							saclassList[thisClass] = saclassList[thisClass] + 1
						else:
							saclassList[thisClass] = 1
			avDump = avDump.keys()
			for key in avDump:
				if key in avList:
					avList[key] = avList[key] + 1
				else:
					avList[key] = 1
		currentFile.close()
		newCurrentFile = open("..\\" + item[:-5], "r", encoding = "latin-1")
		line = newCurrentFile.readline()
		line = newCurrentFile.readline()
		while "***URL***" not in line:
			line = line[:-1]
		#for line in newCurrentFile:
		#	if "***URL***" in line:
		#		newCurrentFile.close()
			if line not in "\n" and line not in "\r\n":
				if line in apiList:
					apiList[line] = apiList[line] + 1
				else:
					apiList[line] = 1
			line = newCurrentFile.readline()
		newCurrentFile.close()
	os.chdir("..\\..")
	avclassFile = open("AVclassTotal.json", "w")
	json.dump(avclassList, avclassFile, indent = 4)
	avclassFile.close()
	msclassFile = open("MSclassTotal.json", "w")
	json.dump(msclassList, msclassFile, indent = 4)
	msclassFile.close()
	saclassFile = open("SAclassTotal.json", "w")
	json.dump(saclassList, saclassFile, indent = 4)
	saclassFile.close()
	avFile = open("avTotal.json", "w")
	json.dump(avList, avFile, indent = 4)
	avFile.close()
	apiFile = open("apiTotal.json", "w")
	json.dump(apiList, apiFile, indent = 4)
	apiFile.close()