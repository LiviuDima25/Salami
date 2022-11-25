
"1." 
"A CSV file is a text file that has a specific format which allows data to be saved in a table structured format."

myNumberString = (input("Please enter 5 numbers separeted by commas: "))

file = open("numList.csv", "w")
file.write(myNumberString)
file.close()
file = open("numList.csv","r")
dataIn = file.read()
file.close()
print(dataIn)
myList = dataIn.split(",")
print(myList)
myList = [int(item) for item in myList]

myList.sort()
print(myList)

print("Min Value: ", min(myList))
print("Max Value: ", max(myList))

import statistics
average=statistics.mean(myList)
print(average)

Names = []
Pets = []

names = input("Whats your name?")
pets = int(input("How many pets do you have?"))

"2."

"Removing unnecesary code that dosent help and let it be all tidy"

"It keeps the cope tidy and clen so that others developers can work freely on it"
"3."

"11100011"


##Anagrams are words that contain the same letters. Eg. car and arc are anagrams of each other 

 

def is_anagram(w1, w2):
  if sorted(w1) == sorted(w2): 
    return True 

  else: 

    return False 

 

word1 = input("Enter the first word: ") 

word2 = input("Enter you second word: ")

word3 = "LISTEN"

word4 = "SILENT"



##Test whether the sorted strings are the same as each other 

##If the sorted strings are the same as each other then they must be anagrams 

 

if(word1, word2) == (word3, word4): 

  print("YES")


if(word1) == (word2):
  print(word1, "is an anagram of", word2)
