# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lilly Woodward
#               Kyle Rex
#               Jesse Garcia
#               Ethan Nguyen
# Section:      516
# Assignment:   Lab 6
# Date:         10/3/2022
#
s = float(input("Enter the side length in meters:"))
n = int(input("Enter the number of layers:"))
total = 0
for i in range(1,n+1):
#calculates area of top
    top = ((3**.5)/4*s**2)*(2*i-1)
#calculates area of the sides
    side = (s**2*i)*3
#adds the area of the top and side together
    total += top + side

print(f"You need {total:.2f} m^2 of gold foil to cover the pyramid")