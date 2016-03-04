"""

This program is a Mapper program. Its function is to go through a text file and
create a list of words that are anagrams. The words are stored in the format
"Key<tab>Value" in an output file. 

1. The program reads the space-separated input text string.
2. It then turns it into a list of strings that were separated by a space.
3. It then does the following:-
        i. Read each string in this list
       ii. Store this string as the Value.
      iii. Sort the characters of this string alphabetically.
       iv. Store the resultant value as the Key.
        v. Write this Key-Value pair in a tab separated format into output file.
       vi. Perform steps i thru v until end of input file.
4. This output file will be taken as the input and the Key-Value pairs will be
   sorted.
5. The sorted Key-Value pairs are written to a new output file which is provided
   as input to the Reducer program.
       
"""

# Open, read and close input file
inputFile    = open("input_anagram.txt", "r")
inputReadStr = inputFile.read()
inputFile.close()

# Open output file in write mode
outputFile   = open("output_anagram.txt", "w")

# Split words in input file using the space in between as a seperator and store
# each word as string in a list called tempList
tempList     = inputReadStr.split(" ")

#print(tempList)

inputCount   = len(tempList)

for i in range(0, inputCount):
# Store the string read from the list as the Value    
  valueStr = tempList[i]
  
# Sort the characters of the above string alphabetically
  holdStr  = sorted(tempList[i])
  
# Store this sorted string as Key
  keyStr = ''.join(holdStr)
  
# Write to output in Key<tab>Value format. Avoid \n on last record being written

  if i == (inputCount - 1):
    outRecord  = keyStr + "\t" + valueStr
  else :
    outRecord  = keyStr + "\t" + valueStr + "\n"
    
  outputFile.write(outRecord)

# Close output file
outputFile.close()


# Open above written output file to read Key-Value pairs

outputFile   = open("output_anagram.txt", "r")
outRead      = outputFile.read()

# Store each line in input line as an element of a list

tempList     = outRead.split("\n")
sortedList   = list(tempList)
tempLen      = len(tempList)
j = 0

for i in range(0, tempLen):
   sortedList[j]  = tempList[i].split("\t")
   j+=1

# The below line of code sorts the elements in the list alphabetically

sortedList = sorted(sortedList)

# Open new output file to store a sorted list of Key-Value pairs

outFileSorted  = open("output_anagram_sorted.txt", "w")

# Convert list elements into strings in the Key<tab>Value format and write to
# new output file. Avoid \n on the last entry.

for i in range(0, len(sortedList)):
   outTempRec = sortedList[i]
   if i == (len(sortedList) - 1):
     outRecSorted = str(outTempRec[0]) + '\t' + str(outTempRec[1])
   else:
     outRecSorted = str(outTempRec[0]) + '\t' + str(outTempRec[1]) + '\n'
   outFileSorted.write(str(outRecSorted))

outFileSorted.close()
print("Sorted Anagram output file written")

