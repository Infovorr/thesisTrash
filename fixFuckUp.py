import os

if __name__ == "__main__":
	os.chdir(".\\evenNewer\\jason")
	jsonList = os.listdir()
	lineListA = []
	lineListB = []
	lineListC = []
	lenA = 0
	lenB = 0
	lenC = 0
	for item in jsonList:
		jsonName = item[:-5]
		apiFileA1 = open("..\\" + jsonName, "r")
		for lineA in apiFileA1:
			lineListA.append(lineA)
		apiFileA1.close()
		lenA = len(lineListA)
		apiFileA2 = open("C:\\apiFiles\\Unique\\" + jsonName, "w")
		for itemA in lineListA:
			apiFileA2.write(itemA)
			if "***Diagnosis***" in itemA:
				break
		apiFileA2.close()
		lineListA.clear()
		apiFileB1 = open("..\\..\\eVectorSamples\\" + jsonName, "r")
		for lineB in apiFileB1:
			#print(lineB)
			lineListB.append(lineB)
		apiFileB1.close()
		lenB = len(lineListB)
		apiFileB2 = open("C:\\apiFiles\\Vector\\" + jsonName, "w")
		for itemB in lineListB:
			apiFileB2.write(itemB)
			if "***Diagnosis***" in itemB:
				break
		apiFileB2.close()
		lineListB.clear()
		apiFileC1 = open("..\\..\\eVectorSamplesU\\" + jsonName, "r")
		for lineC in apiFileC1:
			#print(lineC)
			lineListC.append(lineC)
		apiFileC1.close()
		lenC = len(lineListC)
		apiFileC2 = open("C:\\apiFiles\\VectorNonRep\\" + jsonName, "w")
		for itemC in lineListC:
			apiFileC2.write(itemC)
			if "***Diagnosis***" in itemC:
				break
		apiFileC2.close()
		lineListC.clear()
		#print(jsonName + " " + str(lenA) + " " + str(lenB) + " " + str(lenC))