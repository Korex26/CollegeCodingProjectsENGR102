# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 7b
# Date:         10/14/2022
#
a = str(input("Enter some text:")) #gets input
words = a.split()   #makes the input into a list

leet_speak = {'a':4, 'e':3, 'o':0, 's':5, 't':7} #creates a dictionary of values
print(f'In leet speak, "{a}" is:', end=" ") #prints ininital print statement
for i in words:
    for x in i: 
        if x not in leet_speak:
            print(x, end="")
        if x in leet_speak: #these all add onto the original print statement to give the correctly formated answer
            x = leet_speak[x]
            print(x, end="")
    print(" ", end="") 
#converts required letters into leet
