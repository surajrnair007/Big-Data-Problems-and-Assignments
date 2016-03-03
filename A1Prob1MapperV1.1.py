import sys
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

alphachar = { "a":0,  "b":1 , "c":2 , "d":3 , "e":4 , "f":5 , "g":6 , "h":7 ,
              "i":8,  "j":9 , "k":10, "l":11, "m":12, "n":13, "o":14, "p":15,
              "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22,
              "x":23, "y":24, "z":25 }


#Initializing lists and strings

charcount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
letter    = 0

#Opening and reading input file

#inputfile = open("inputfile_small.txt", "r")
inputfile = sys.argv[1]
open(inputfile, "r")
intext    = inputfile.read()

try:
 for letter in range(len(intext)):
    if intext[letter].lower() in "abcdefghijklmnopqrstuvwxyz":
       charcount[alphachar[intext[letter].lower()]] += 1         


 outputfile = open("outputfile.txt", "w")
 finalcount = str(charcount)
 print(finalcount)
 outputfile.write(finalcount)

finally:
# Ensure all files are closed
 outputfile.close()
 inputfile.close()
