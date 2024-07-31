# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kyle Rex
#               Ethan Nguyen
#               Jesse Garcia
#               Lilly Woodward
# Section:      516
# Assignment:   Lab 2a - team
# Date:         07/09/2022

import math

# Part 1

x1 = 10
y1 = 2025
y2 = 23025
x2 = 55
t = 25
x0 = x2-x1
if x1 <= x0 <= x2:
    y0 = y2-y1
    ans = (y0 / x0) * (t - x1) + y1
    print("Part 1:")
    print("For t = " + str(t) +" minutes, the position p = " + str(ans) + " kilometers")
else:
    print("error")

# Part 2

t = 60*5
r = 6745
circle = 2*math.pi*r
if x1 <= x0 <= x2:
    y0 = y2-y1
    ans = (y0 / x0) * (t - x1) + y1
    ans %= circle
    print("Part 2:")
    print("For t = 5.0 hours, the position p = " + str(ans) + " kilometers")
else:
    print("error")
