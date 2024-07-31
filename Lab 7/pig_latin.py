# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 7b
# Date:         10/14/2022
#
a = str(input("Enter word(s) to convert to Pig Latin:"))
pig_latin = a.split()    #makes the input into a list
for i in range(len(pig_latin)):
    pig_latin[i] = [pig_latin[i]] #breaks down that list into another list
    
for i in range(len(pig_latin)):
    if pig_latin[i][0][0] == "a" or pig_latin[i][0][0] == "e" or pig_latin[i][0][0] == "i" or pig_latin[i][0][0] == "o" or pig_latin[i][0][0] == "u" or pig_latin[i][0][0] == "y":
        pig_latin[i][0] += "yay" # adds yay to the ends of words that begin with a vowel
    else:
        for x in range(len(pig_latin[i][0])): 
         if pig_latin[i][0][x] != "a" and pig_latin[i][0][x] != "e" and pig_latin[i][0][x] != "i" and pig_latin[i][0][x] != "o" and pig_latin[i][0][x] != "u" and pig_latin[i][0][x] != "y":
            pig_latin[i][0] += pig_latin[i][0][x] # adds the consonant to the end of the word until it finds a vowel and stops
         else:
             break
            
        pig_latin[i][0] += "ay" #adds ay to the end of the word
        pig_latin[i][0] = pig_latin[i][0][x:len(pig_latin[i][0])] # takes the required segment of the word to be outputed ( gets rid of the first part of the word you dont need anymore)


print(f'In Pig Latin, "{a}" is:', end=" ")
for i in range(len(pig_latin)): # prints out the required output in the correct format
   print(pig_latin[i][0], end=" ")

