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
x = float(input("Enter the excess temperature:"))
if 1.3 <= x < 5.0:#when x is between 1.3 and 5
    x0 = 1.3 #value of x at point A
    y0 = 1000 #value of y at point A
    x1 = 5 #value of x at point B
    y1 = 7000 #value of y at point B
    m = (log(y1/y0 )) / (log(x1/x0 ))# given equation for linear interpolation 
    y = y0 * (x/x0 )**m# given equation for linear interpolation 
    print("The surface heat flux is approximately", int(round(y,0)), "W/m^2")#rounds y to a whole number and makes it a integer
if 5.0 <= x < 30.0:#when x is between 5 and 30
    x0 = 5 #value of x at point B
    y0 = 7000 #value of y at point B
    x1 = 30 #value of x at point C
    y1 = 1.5*10**6 #value of y at point C
    m = (log(y1/y0 )) / (log(x1/x0 ))# given equation for linear interpolation 
    y = y0 * (x/x0 )**m# given equation for linear interpolation 
    print("The surface heat flux is approximately", int(round(y,0)), "W/m^2")#rounds y to a whole number and makes it a integer
if 30 <= x < 120:#when x is between 30 and 120
    x0 = 30 #value of x at point C
    y0 = 1.5*10**6 #value of y at point C
    x1 = 120 #value of x at point D
    y1 = 2.5*10**4 #value of y at point D
    m = (log(y1/y0 )) / (log(x1/x0 )) # given equation for linear interpolation 
    y = y0 * (x/x0 )**m# given equation for linear interpolation 
    print("The surface heat flux is approximately", int(round(y,0)), "W/m^2")#rounds y to a whole number and makes it a integer
if 120 <= x <= 1200: #when x is between 120 and 1200
    x0 = 120 #value of x at point D
    y0 = 2.5*10**4 #value of y at point D
    x1 = 1200 #value of x at point E
    y1 = 1.5*10**6 #value of y at point E
    m = (log(y1/y0 )) / (log(x1/x0 ))# given equation for linear interpolation 
    y = y0 * (x/x0 )**m# given equation for linear interpolation 
    print("The surface heat flux is approximately", int(round(y,0)), "W/m^2")#rounds y to a whole number and makes it a integer
if x > 1200 or x < 1.3:#when x is greater than 1200 or less than 1.3
    print("Surface heat flux is not available") # graph ends at those x values so there are no y values
