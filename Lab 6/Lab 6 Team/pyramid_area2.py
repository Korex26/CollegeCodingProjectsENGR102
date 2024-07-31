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
# variables and inputs
import math
from math import *
side_length = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))

#number of faces on each layer
faces = (layers / 2) * (3 + (layers *3))

#area of the faces
a_faces = faces * (side_length * side_length)

#area of the top
top = (layers * layers) * (sqrt(3) / 4) * (side_length**2)
total_area = top + a_faces

print(f'You need {total_area:.2f} m^2 of gold foil to cover the pyramid')