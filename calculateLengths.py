import json
import os

if __name__ == "__main__":
	UORfile = []
	UC1file = []
	UC2file = []
	EORfile = []
	EC1file = []
	EC2file = []
	NORfile = []
	NC1file = []
	NC2file = []
	
	UORdict = {}
	UC1dict = {}
	UC2dict = {}
	EORdict = {}
	EC1dict = {}
	EC2dict = {}
	NORdict = {}
	NC1dict = {}
	NC2dict = {}
	
	thisFile = open("uniqueOrig.csv", "r")
	for line in thisFile:
		UORfile.append(line.split(","))
	thisFile.close()
	thisFile = open("uniqueCmp1.csv", "r")
	for line in thisFile:
		UC1file.append(line.split(","))
	thisFile.close()
	thisFile = open("uniqueCmp2.csv", "r")
	for line in thisFile:
		UC2file.append(line.split(","))
	thisFile.close()
	thisFile = open("vectorOrig.csv", "r")
	for line in thisFile:
		EORfile.append(line.split(","))
	thisFile.close()
	thisFile = open("vectorCmp1.csv", "r")
	for line in thisFile:
		EC1file.append(line.split(","))
	thisFile.close()
	thisFile = open("vectorCmp2.csv", "r")
	for line in thisFile:
		EC2file.append(line.split(","))
	thisFile.close()
	thisFile = open("vectnrOrig.csv", "r")
	for line in thisFile:
		NORfile.append(line.split(","))
	thisFile.close()
	thisFile = open("vectnrCmp1.csv", "r")
	for line in thisFile:
		NC1file.append(line.split(","))
	thisFile.close()
	thisFile = open("vectnrCmp2.csv", "r")
	for line in thisFile:
		NC2file.append(line.split(","))
	thisFile.close()
	
	for row in UORfile:
		size = str(len(row))
		if size in UORdict:
			UORdict[size] += 1
		else:
			UORdict[size] = 1
	
	for row in EORfile:
		size = str(len(row))
		if size in EORdict:
			EORdict[size] += 1
		else:
			EORdict[size] = 1
	
	for row in NORfile:
		size = str(len(row))
		if size in NORdict:
			NORdict[size] += 1
		else:
			NORdict[size] = 1
	
	for row in UC1file:
		size = str(len(row))
		if size in UC1dict:
			UC1dict[size] += 1
		else:
			UC1dict[size] = 1
	
	for row in NC1file:
		size = str(len(row))
		if size in NC1dict:
			NC1dict[size] += 1
		else:
			NC1dict[size] = 1
	
	for row in EC1file:
		size = str(len(row))
		if size in EC1dict:
			EC1dict[size] += 1
		else:
			EC1dict[size] = 1
	
	for row in UC2file:
		size = str(len(row))
		if size in UC2dict:
			UC2dict[size] += 1
		else:
			UC2dict[size] = 1
	
	for row in NC2file:
		size = str(len(row))
		if size in NC2dict:
			NC2dict[size] += 1
		else:
			NC2dict[size] = 1
	
	for row in EC2file:
		size = str(len(row))
		if size in EC2dict:
			EC2dict[size] += 1
		else:
			EC2dict[size] = 1
	
	os.chdir("lengths")
	
	newFile = open("UOR.json", "w")
	json.dump(UORdict, newFile, indent = 4)
	newFile.close()
	
	newFile = open("EOR.json", "w")
	json.dump(EORdict, newFile, indent = 4)
	newFile.close()
	
	newFile = open("NOR.json", "w")
	json.dump(NORdict, newFile, indent = 4)
	newFile.close()
	
	newFile = open("UC1.json", "w")
	json.dump(UC1dict, newFile, indent = 4)
	newFile.close()
	
	newFile = open("EC1.json", "w")
	json.dump(EC1dict, newFile, indent = 4)
	newFile.close()
	
	newFile = open("NC1.json", "w")
	json.dump(NC1dict, newFile, indent = 4)
	newFile.close()
	
	newFile = open("UC2.json", "w")
	json.dump(UC2dict, newFile, indent = 4)
	newFile.close()
	
	newFile = open("EC2.json", "w")
	json.dump(EC2dict, newFile, indent = 4)
	newFile.close()
	
	newFile = open("NC2.json", "w")
	json.dump(NC2dict, newFile, indent = 4)
	newFile.close()