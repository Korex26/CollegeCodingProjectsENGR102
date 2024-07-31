# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 3b
# Date:         09/14/2022
#
import math
from math import *

print("This program calculates the applied force given mass and acceleration")
m = input('Please enter the mass (kg): ')
a = input('Please enter the acceleration (m/s^2): ') 
force = [m, a]
x= float(force[0])
y= float(force[1])
print("Force is", round(x * y, 1), "N")

print("This program calculates the wavelength given distance and angle")
d = input('Please enter distance (nm): ') 
a = input('Please enter the angle (degrees): ') 
wavelength = [d, a]
x= float(wavelength[0])
y= float(wavelength[1])
print("Wavelength is", round(2 * x * (sin(radians(y))), 5), "nm")

print("This program calculates how much Radon-222 is left given time and initial amount")
g = input('Please enter the initial amount (g): ') 
d = input ("Please enter the time (days): ")
amount = [g, d]
x= float(amount[0])
y= float(3.8)
z= float(amount[1])
print("Radon-222 left is", round(x*2**(-z/y), 2), "g")

print("This program calculates the pressure given moles, volume, and temperature")
m = input('Please enter the number of moles (moles): ') 
k = input('Please enter the temperature (kelvin): ') 
v = input("Please enter the volume (m^3): ")
presure = [m, k, v]
x= float(presure[0])
y= float(presure[1])
z= float(presure[2])
t= float(8.314) #m^3Pa/K·mol
g= float(1000) #conversion constant 
print("Radon-222 left is", round(((((x * t * y))/ z) / g), 0), "kPa")