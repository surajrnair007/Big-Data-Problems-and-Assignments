"""

This is the Reducer program that displays the anagrams of a word in a text file.
The input to this program is a file consisting of tab-separated Key-Value pairs 
that have already been sorted.

The program displays each word and their corresponding anagrams, if any.

"""

#inputFile    = open("output_anagram_sorted.txt", "r")
inputFile    = open("output_anagram_sorted1.txt", "r")
inputReadStr = inputFile.read()
tempList     = inputReadStr.split("\n")

inputList    = list(tempList)
tempLen      = len(tempList)
anagramCount = 0
j            = 0

for i in range(0, tempLen):
    inputList[j] = tempList[i].split("\t")
    j+=1

tempKey      = inputList[0][0]
tempValue    = inputList[0][1]
firstTimeFlag = 1

print("The following are the list of anagrams:- " + "\n")

for i in range(1, tempLen):
    if inputList[i][0]  == tempKey :
       if firstTimeFlag == 1:
          anagramList   = tempKey + "  -  " + tempValue + " " + inputList[i][1]
          anagramCount  = 2
          firstTimeFlag = 0
       else:
          anagramList   = anagramList + " " + inputList[i][1]
          anagramCount+=1
       if ((i == (tempLen - 1)) and (anagramCount > 1)):
          print(anagramList)
    else:
       if anagramCount > 1:
          print(anagramList)
           
       tempKey         = inputList[i][0]
       tempValue       = inputList[i][1]
       firstTimeFlag   = 1
       anagramCount    = 0

inputFile.close()
