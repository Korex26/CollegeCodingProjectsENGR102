# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lilly Woodward
#               Kyle Rex
#               Jesse Garcia
#               Ethan Nugyen
# Section:      516
# Assignment:   Lab 12
# Date:         11 21 2022
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np

# create the matrices
matrix_a = np.arange(12).reshape(3, 4)
matrix_b = np.arange(8).reshape(4, 2)
matrix_c = np.arange(6).reshape(2, 3)
matrix_ab = matrix_a.dot(matrix_b)
matrix_d = matrix_ab.dot(matrix_c)
matrix_dt = matrix_d.T
matrix_e = np.sqrt(matrix_d)/2

# print all the matrices
print('A = ', matrix_a)
print()
print('B = ', matrix_b)
print()
print('C = ', matrix_c)
print()
print('D = ', matrix_d)
print()
print('D^T = ', matrix_dt)
print()
print('E = ', matrix_e)