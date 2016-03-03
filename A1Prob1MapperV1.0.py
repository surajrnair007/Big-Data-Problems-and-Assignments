"""
This program does the following:-
    1. Reads the text from the input file.
    2. Compares each character from input text to a pre-defined dictionary
       to see if it is a letter of the alphabet.
    3. If a letter of the alphabet is found, a count corresponding to the
       position of that letter in the alphabet is incremented in an array.
    4. The array containing the total count of each letter is written to an
       output file. This output file will be one of the inputs to the Reducer.
"""


#Defining a dictionary containing each letter of the alphabet

alphaChar = { "a":0,  "b":1 , "c":2 , "d":3 , "e":4 , "f":5 , "g":6 , "h":7 ,
              "i":8,  "j":9 , "k":10, "l":11, "m":12, "n":13, "o":14, "p":15,
              "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22,
              "x":23, "y":24, "z":25 }


#Initializing lists and strings 

charCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
letter    = 0

#Opening and reading input file

inputFile = open("inputfile_small.txt", "r")
inText    = inputFile.read()

try:
 for letter in range(len(inText)):
    if inText[letter].lower() in "abcdefghijklmnopqrstuvwxyz":
       charCount[alphaChar[inText[letter].lower()]] += 1         


 outputFile = open("outputfile.txt", "w")
 finalCount = str(charCount)
 print(finalCount)
 outputFile.write(finalCount)

finally:
# Ensure all files are closed
 outputFile.close()
 inputFile.close()
