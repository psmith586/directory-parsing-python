#Author: Phillip Smith
#recursive keyword search/directory data display

#using os library to walk the directory 
import os
#using matplotlib to create xy graph of data
import matplotlib.pyplot as plt

#init root dir and keyword vars from user
root_dir = input("Please enter directory path: ")
keyword = input("Please enter keyword: ")

#this method will be used to accumulate files with the keyword and populate array
def CheckKey(r, k):
	#will accumulate number of files with keyword
	total = 0
	#populate array with the sub dirs and the number of files with keyword
	arr = {}
	
	#check dirs/subdirs for files 
	for fname in os.listdir(r):
		#use join to create the new path to check on each iteration
		newPath = os.path.join(r, fname)
		#this will confirm an object in the dir is a txt file to be read
		if os.path.isfile(newPath):
			#strip the file name out to check if it contains keyword
			s = newPath.split('\\')[-1].split('.')[0]
			#if the keyword is in the current file name and contents increment total
			if k in s and k in open(newPath, 'r').read():
				total += 1
		
		#add the number value to associate with the dir key
		arr[r] = total
		
	#return each key/value object tot final array	
	return arr[r]			
	
#init new array to recursively add results
finalArr = {}
	
#use os walk and searchkey to search through dirs, subdirs, files
for root, dirs, files in os.walk(root_dir):
	finalArr[root] = CheckKey(root, keyword)
	
#display final array
print("Number of Files Containing Keyword by Directory: ", finalArr)

#break finalArr into a seperate arrays
#x = keys, y = values
x = []
y = []

#iterate through each key/value pair and append to new arrays
for key, value in finalArr.items():
	x.append(key)
	y.append(value)
	
#use matplotlib to display line graph of data		
plt.plot(x,y)
plt.show()
	

	


	