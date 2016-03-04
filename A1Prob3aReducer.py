"""

This is the Reducer program that displays the list of users with the same DNA
sequence grouped together.

The input to this program is a file consisting of tab-separated Key-Value pairs 
that have already been sorted. Here DNA seq value is the Key and the username is
the Value

The program displays each DNA seq and the list of users having that DNA sequnce.
It also stores the same in an output file.

"""

#inputFile    = open("output_anagram_sorted.txt", "r")
inputFile    = open("output_same_DNAseq.txt", "r")
inputReadStr = inputFile.read()
tempList     = inputReadStr.split("\n")

inputList    = list(tempList)
tempLen      = len(tempList)
userCount    = 0
j            = 0

for i in range(0, tempLen):
    inputList[j] = tempList[i].split("\t")
    j+=1

tempKey      = inputList[0][0]
tempValue    = inputList[0][1]
firstTimeFlag = 1

outputFile    = open("output_same_DNAseq_list.txt", "w")

print("The following are the list of users with the same DNA seq :- " + "\n")

for i in range(1, tempLen):
    if inputList[i][0]  == tempKey :
       if firstTimeFlag == 1:
          userList      = tempKey + "  -  " + tempValue + " " + inputList[i][1]
          userCount     = 2
          firstTimeFlag = 0
       else:
          userList      = userList + " " + inputList[i][1]
          userCount+=1
       if ((i == (tempLen - 1)) and (userCount > 1)):
          print(userList) 
          outputFile.write(userList)
    else:
       if userCount > 1:
          print(userList)
          if (i != (tempLen - 1)):
             userList      = userList + "\n"
          outputFile.write(userList)
       else:
          if (i != (tempLen - 1)):
             userList      = tempKey + "  -  " + tempValue + "\n"
             
          if (i == (tempLen - 1)):
             userList      = tempKey + "  -  " + tempValue + "\n"
             print(userList)
             outputFile.write(userList)
             
             userList      =  str(inputList[i][0]) + " - " + str(inputList[i][1])
             
          print(userList)
          outputFile.write(userList)
           
       tempKey         = inputList[i][0]
       tempValue       = inputList[i][1]
       firstTimeFlag   = 1
       userCount       = 0

inputFile.close()
outputFile.close()
