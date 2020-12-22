import json
import os
import requests
import time

if __name__ == "__main__":
	oldHashes = open("remainingHashes.txt", "r")
	fileList = []
	for line in oldHashes:
		fileList.append(line)
	oldHashes.close()
	
	url = "https://www.virustotal.com/vtapi/v2/file/report"
	for i in range(1000):
		params = {"apikey": "", "resource": fileList[i][:-1] }
		response = requests.get(url, params = params)
		report = response.json()
		result = open(".\\evenNewer\\jason\\" + fileList[i][:-1] + ".json", "w")
		json.dump(report, result, indent = 4)
		result.close()
		print("Wrote report for " + fileList[i][:-1])
		time.sleep(15)
	
	newHashes = open("remainingHashes.txt", "w")
	i = 1000
	while i < len(fileList):
		newHashes.write(fileList[i])
		i += 1
	newHashes.close()