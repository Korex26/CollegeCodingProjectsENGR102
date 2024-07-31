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
# As a team, we have gone through all required sections of the matplotlib tutorial, and each team member understands the material
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2,2.0001,0.01)
x_cubic = np.arange(-4, 4.1, 0.32)
x_sin = np.arange(-2*np.pi, 2*np.pi + 0.001, 0.01)
#y = (1/4*f)*x**2
plt.figure(1)
plt.plot(x, (1/(4*2))*x**2, 'r', linewidth=2, label='f=2')
plt.plot(x, (1/(4*6))*x**2, 'b', linewidth=6, label='f=6')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Parabola plots with varying focal length')
plt.figure(2)
plt.plot(x_cubic,(2*x_cubic**3+3*x_cubic**2-11*x_cubic-6),'y*')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Plot of cubic polynomial')
plt.figure(3)
plt.subplot(211)
plt.title('Plot of cos(x) and sin(x)')
plt.xlim([-2*np.pi - 1, 2*np.pi + 1])
plt.plot(x_sin, np.cos(x_sin), 'r')
plt.ylabel('y=cos(x)')
plt.grid()
plt.subplot(212)
plt.xlim([-2*np.pi - 1, 2*np.pi + 1])
plt.plot(x_sin, np.sin(x_sin), 'b')
plt.xlabel('x')
plt.ylabel('y=sin(x)')
plt.grid()
plt.show()
