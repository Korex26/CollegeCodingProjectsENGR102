# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 30
# Date:         10/30/2022
#
x = int(input("Please insert the maxium of the range:"))
#input 100
y = int(input("Please insert the minimum of the range:"))
#input 30
List = []
List2 = []
for i in range(x): #Gives me a range of numbers
    List.append(i+1)
for i in range(y):
    List.remove(i+1)

for i in range(len(List)):
    if (List[i] % 5 == 0) and (List[i] % 7 == 0):
        List2.append(List[i])

print(List2)

#Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers