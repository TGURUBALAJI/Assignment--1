
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
import math

#if using termux
import subprocess
import shlex
#end if

#2Angles and 1side
angle_a = 60
angle_b = 50
side_b = 7

#Calculate the third angle
angle_c = abs(180-(angle_a + angle_b))

#Using sine rule for sine multiplication factor
#sine_factor = side_b/math.sin(math.radians(angle_b))
CD=side_b * math.sin(math.radians(angle_a))
a=CD/math.sin(math.radians(angle_b))
AD=side_b*math.cos(math.radians(angle_a))
BD=a*math.cos(math.radians(angle_b))
c=AD+BD

#Triangle vertices
A = np.array([0,0]) 
B = np.array([c,0]) 
C = np.array([AD,CD]) 

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
