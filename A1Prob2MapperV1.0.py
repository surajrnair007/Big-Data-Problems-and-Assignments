"""

This program is a Mapper program. Its function is to go through a text file and
create a list of words that are anagrams. The words are stored in the format
"Key<tab>Value" in an output file. This output file will be taken as the input
to the Reducer program.

1. The program reads the space-separated input text string.
2. It then turns it into a list of strings that were separated by a space.
3. It then does the following:-
        i. Read each string in this list
       ii. Store this string as the Value.
      iii. Sort the characters of this string alphabetically.
       iv. Store the resultant value as the Key.
        v. Write this Key-Value pair in a tab separated format into output file.
       vi. Perform steps i thru v until end of inout file.
       
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
  
# Write to output in Key<tab>Value format
  outRecord  = keyStr + "\t" + valueStr + "\n"
  print outRecord
  outputFile.write(outRecord)

# Close output file
outputFile.close()
