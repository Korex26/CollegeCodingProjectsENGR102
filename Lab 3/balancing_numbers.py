# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 3b
# Date:         10/3/2022
#
a = int(input("Enter a value for n: "))
n=1
b=0
while n != a: # This while statement is the sum of numbers from 1 to (n-1)
    b+= n
    n +=1

c = a + 1 # This is because of the (n+1)
r = 0
d = 0
while d < b: # This while statement is the sum of numbers (n+1) to (n+r)
    r+=1
    d += c 
    c += 1

if d == b:    
    print (n, "is a balancing number with r=", r)
else:
    print(n, "is not a balancing number")
    