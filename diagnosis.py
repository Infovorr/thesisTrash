import json
import os

if __name__ == "__main__":
	os.chdir(".\\evenNewer\\jason")
	jsonList = os.listdir()
	jsonDict = {}
	for item in jsonList:
		apiFileA = ""
		apiFileB = ""
		apiFileC = ""
		print("Starting " + item)
		jsonFile = open(item, "r")
		jsonDict = json.load(jsonFile)
		jsonFile.close()
		jsonName = item[:-5]
		apiFileA = open("C:\\apiFiles\\Unique\\" + jsonName, "a")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "Avast" in subDict:
				subDict = subDict["Avast"]
				if subDict["detected"]:
					diag = subDict["result"]
					if "[" in diag:
						diag = diag[(diag.index("[") + 1):(diag.index("]"))]
						apiFileA.write(diag + "\n")
					else:
						apiFileA.write("||||||Avast||||||\n")
				else:
					apiFileA.write("||||||Avast||||||\n")
			else:
				apiFileA.write("||||||Avast||||||\n")
		else:
			apiFileA.write("||||||Avast||||||\n")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "Microsoft" in subDict:
				subDict = subDict["Microsoft"]
				if subDict["detected"]:
					diag = subDict["result"]
					if ":" in diag:
						diag = diag[:diag.index(":")]
						apiFileA.write(diag + "\n")
					else:
						apiFileA.write("||||||Microsoft||||||\n")
				else:
					apiFileA.write("||||||Microsoft||||||\n")
			else:
				apiFileA.write("||||||Microsoft||||||\n")
		else:
			apiFileA.write("||||||Microsoft||||||\n")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "SUPERAntiSpyware" in subDict:
				subDict = subDict["SUPERAntiSpyware"]
				if subDict["detected"]:
					diag = subDict["result"]
					if "." in diag:
						diag = diag[:diag.index(".")]
						apiFileA.write(diag + "\n")
					else:
						apiFileA.write("||||||SUPERAntiSpyware||||||\n")
				else:
					apiFileA.write("||||||SUPERAntiSpyware||||||\n")
			else:
				apiFileA.write("||||||SUPERAntiSpyware||||||\n")
		else:
			apiFileA.write("||||||SUPERAntiSpyware||||||\n")
		apiFileA.close()
		apiFileB = open("C:\\apiFiles\\Vector\\" + jsonName, "a")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "Avast" in subDict:
				subDict = subDict["Avast"]
				if subDict["detected"]:
					diag = subDict["result"]
					if "[" in diag:
						diag = diag[(diag.index("[") + 1):(diag.index("]"))]
						apiFileB.write(diag + "\n")
					else:
						apiFileB.write("||||||Avast||||||\n")
				else:
					apiFileB.write("||||||Avast||||||\n")
			else:
				apiFileB.write("||||||Avast||||||\n")
		else:
			apiFileB.write("||||||Avast||||||\n")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "Microsoft" in subDict:
				subDict = subDict["Microsoft"]
				if subDict["detected"]:
					diag = subDict["result"]
					if ":" in diag:
						diag = diag[:diag.index(":")]
						apiFileB.write(diag + "\n")
					else:
						apiFileB.write("||||||Microsoft||||||\n")
				else:
					apiFileB.write("||||||Microsoft||||||\n")
			else:
				apiFileB.write("||||||Microsoft||||||\n")
		else:
			apiFileB.write("||||||Microsoft||||||\n")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "SUPERAntiSpyware" in subDict:
				subDict = subDict["SUPERAntiSpyware"]
				if subDict["detected"]:
					diag = subDict["result"]
					if "." in diag:
						diag = diag[:diag.index(".")]
						apiFileB.write(diag + "\n")
					else:
						apiFileB.write("||||||SUPERAntiSpyware||||||\n")
				else:
					apiFileB.write("||||||SUPERAntiSpyware||||||\n")
			else:
				apiFileB.write("||||||SUPERAntiSpyware||||||\n")
		else:
			apiFileB.write("||||||SUPERAntiSpyware||||||\n")
		apiFileB.close()
		apiFileC = open("C:\\apiFiles\\VectorNonRep\\" + jsonName, "a")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "Avast" in subDict:
				subDict = subDict["Avast"]
				if subDict["detected"]:
					diag = subDict["result"]
					if "[" in diag:
						diag = diag[(diag.index("[") + 1):(diag.index("]"))]
						apiFileC.write(diag + "\n")
					else:
						apiFileC.write("||||||Avast||||||\n")
				else:
					apiFileC.write("||||||Avast||||||\n")
			else:
				apiFileC.write("||||||Avast||||||\n")
		else:
			apiFileC.write("||||||Avast||||||\n")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "Microsoft" in subDict:
				subDict = subDict["Microsoft"]
				if subDict["detected"]:
					diag = subDict["result"]
					if ":" in diag:
						diag = diag[:diag.index(":")]
						apiFileC.write(diag + "\n")
					else:
						apiFileC.write("||||||Microsoft||||||\n")
				else:
					apiFileC.write("||||||Microsoft||||||\n")
			else:
				apiFileC.write("||||||Microsoft||||||\n")
		else:
			apiFileC.write("||||||Microsoft||||||\n")
		if "scans" in jsonDict:
			subDict = jsonDict["scans"]
			if "SUPERAntiSpyware" in subDict:
				subDict = subDict["SUPERAntiSpyware"]
				if subDict["detected"]:
					diag = subDict["result"]
					if "." in diag:
						diag = diag[:diag.index(".")]
						apiFileC.write(diag + "\n")
					else:
						apiFileC.write("||||||SUPERAntiSpyware||||||\n")
				else:
					apiFileC.write("||||||SUPERAntiSpyware||||||\n")
			else:
				apiFileC.write("||||||SUPERAntiSpyware||||||\n")
		else:
			apiFileC.write("||||||SUPERAntiSpyware||||||\n")
		apiFileC.close()