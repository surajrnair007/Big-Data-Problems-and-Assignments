
""" 
This program acts as the Reducer for the Mapper that computes the count of each
letter in the alphabet in an imput text file.

This program functions as follows:-

1. Each Mapper creates a file in the format "outputfileN.txt" where
   the N represents an integer. E.g. outputfile1.txt, outputfile2.txt, etc.
   These files act as the input files for this Reducer program.

2. All input files contain a string where:-
      i. the first character is a opening square bracket, [
     ii. the last character is a closing square bracket, ]
    iii. the characters in between are numbers stored as strings in a
         comma-separated format.
         
3. This Reducer program opens each input file, reads it,stores
   the content in a string and then closes the file.

4. The program then removes the opening and closing square brackets from the
   string.

5. It then converts this comma-separated string into a list of integers. These
   integers are added to a list called sumList.

6. The program performs steps 3 thru 5 above in a loop until all input strings
   are read.

7. At the end of the above mentioned loop, the program displays the count of
   each letter of the alphabet using sumList.
   
"""

for i in range(1,4):
#i=1
 inputFile  = open("outputfile"+str(i)+".txt", "r")
 inputArray = inputFile.read()
 inputFile.close()
 
#Removing opening and closing square brackets from input string
 inputArray = inputArray[1:-1]

#Convert input string into comma seperated list
 tempList   = inputArray.split(',')

#Convert list of strings into list of integers

 for j in range(0, len(tempList)):
      tempList[j] = int(tempList[j])

#For the first file, copy input list of letter counts into the list sumList.
#For every other file, add counts from new file to existing counts in sumList.

 if i == 1:
    sumList = tempList
 else:
    for k in range(0, len(tempList)):
          sumList[k] = sumList[k] + tempList[k]         

#print sumList 

print ("The final aggregated count of characters \n")
print ("Count of 'a' :  " + str(sumList[0]) + "\n")
print ("Count of 'b' :  " + str(sumList[1]) + "\n")
print ("Count of 'c' :  " + str(sumList[2]) + "\n")
print ("Count of 'd' :  " + str(sumList[0]) + "\n")
print ("Count of 'e' :  " + str(sumList[1]) + "\n")
print ("Count of 'f' :  " + str(sumList[2]) + "\n")
print ("Count of 'g' :  " + str(sumList[0]) + "\n")
print ("Count of 'h' :  " + str(sumList[1]) + "\n")
print ("Count of 'i' :  " + str(sumList[2]) + "\n")
print ("Count of 'j' :  " + str(sumList[0]) + "\n")
print ("Count of 'k' :  " + str(sumList[1]) + "\n")
print ("Count of 'l' :  " + str(sumList[2]) + "\n")
print ("Count of 'm' :  " + str(sumList[0]) + "\n")
print ("Count of 'n' :  " + str(sumList[1]) + "\n")
print ("Count of 'o' :  " + str(sumList[2]) + "\n")
print ("Count of 'p' :  " + str(sumList[0]) + "\n")
print ("Count of 'q' :  " + str(sumList[1]) + "\n")
print ("Count of 'r' :  " + str(sumList[2]) + "\n")
print ("Count of 's' :  " + str(sumList[0]) + "\n")
print ("Count of 't' :  " + str(sumList[1]) + "\n")
print ("Count of 'u' :  " + str(sumList[2]) + "\n")
print ("Count of 'v' :  " + str(sumList[0]) + "\n")
print ("Count of 'w' :  " + str(sumList[1]) + "\n")
print ("Count of 'x' :  " + str(sumList[2]) + "\n")
print ("Count of 'y' :  " + str(sumList[0]) + "\n")
print ("Count of 'z' :  " + str(sumList[1]) + "\n")

