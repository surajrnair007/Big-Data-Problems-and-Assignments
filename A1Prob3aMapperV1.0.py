"""

This is a mapper program. It reads an input file which is in the format
Username<space>DNAseq.

The program considers the DNA seq as Key and Username as the Value. It sorts the
records on the DNA seq and then stores each record in the output file in the
format DNAseq<tab>Username

"""

# Open and read input file

inputFile = open("input_same_DNAseq.txt", "r")
inputRead = inputFile.read()

# Store each line in input line as an element of a list

tempList     = inputRead.split("\n")
sortedList   = list(tempList)
reverseList  = list(tempList)
tempLen      = len(tempList)
j = 0

# Store each group of User and DNA seq as an element of the 2D array

for i in range(0, tempLen):
    sortedList[j]  = tempList[i].split(" ")
    j+=1

# In each element of the 2D array everse elements to store as 'DNA seq, User'

for i in range(0, tempLen):
    sortedList[i][0], sortedList[i][1] = sortedList[i][1], sortedList[i][0]

# The below line of code sorts the elements in the list alphabetically

sortedList = sorted(sortedList)

# Open output file in write mode
outputFile   = open("output_same_DNAseq.txt", "w")

for i in range(0, len(sortedList)):

# Store the string read from the list as the Value
  keyStr = sortedList[i][0]
  valueStr = sortedList[i][1]

# Write to output in Key<tab>Value format. Avoid \n on last entry
  if i == (len(sortedList) - 1):
     outRecord  = keyStr + "\t" + valueStr
  else:   
     outRecord  = keyStr + "\t" + valueStr + "\n"
  outputFile.write(outRecord)

outputFile.close()
