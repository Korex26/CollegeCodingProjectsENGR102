# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 2b
# Date:         09/07/2022
#
from math import *

print("PART A:")
print("Name: Kyle Rex")
print("UIN: 932008894")
print("Section number: 516")
print("Summary of the assignment:I revised my code from a previous assignment to include comments, names of the equations, input variables and the corresponding units in order to add functionality to the code.")
print()

print("PART B through E:")
a1 = 3
a2 = 5.5
a = a1 * a2 
# Name of Equation: Newtons Second Law (a) // F = ma
#Input variables with corresponding units: a1 (m) = mass 3 kg, a2 (a) = acceleration 5.5 m/s^2 
b1 = 2
b2 = 0.025
b3 = sin(radians(25))
b = b1 * b2 * b3
# Name of Equation: Bragg's Law (b) // nλ = 2d sin⁡θ
#Input variables with corresponding units: b1 (2) = constant in Bragg's law 2 (no units), b2 (d) = distance between crystal layers of 0.025 nm, b3 (sin⁡θ) = scattering angle of 25 degrees
c1 = 5
c2 = 2
c3 = (-3/3.8)
c = c1 * c2**c3
# Name of Equation: Radioactive Decay Equation (c) // N(t) = N_0 2^(-t/t_(1/2) )
#Input variables with corresponding units: c1 (N_0) = initial amount of 5 g, c2 (2) = constant in Radioactive Decay Equation 2 (no units), c3 (-t/t_(1/2) ) = 3 days of radioactive decay (t) over half-life of 3.8 days (t_(1/2))
d1 = 5
d2 = 8.314
d3 = 415
d4 = 0.25
d5 = 1000
d = ((d1 * d2 * d3)/ d4) / d5
# Name of Equation: Ideal Gas Law (d) // P = (nRT)/V
#Input variables with corresponding units: d1 (n) = 5 moles , d2 (R) = 8.314 m^3Pa/K·mol for the gas constant, d3 (T) = temperature of 415 K, d4 (V) = volume of 0.25 m^3, d5 = conversion constant
print("Force is",a,"N")
#Output variables: F
print("Wavelength is",b,"nm")
#Output variables: nλ
print("Radon-222 left is",c,"g")
#Output variables: N(t)
print("Pressure is",d,"kPa")
#Output variables: P