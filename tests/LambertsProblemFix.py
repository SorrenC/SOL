# imports 
import sys
sys.path += ['C:/Users/sorre/Desktop/Programs/SOL/src/Functions','C:/Users/sorre/Desktop/Programs/SOL/src/Constants']
import math
import numpy as np
from numpy.linalg import norm 
from Exceptions import *

# Data
r1        = [-1.591163034225527E+08,1.892356715610578E+08,7.870476085229695E+06]  # [km]
r2        = [-1.666285496079473E+08,1.832649379659352E+08,7.929803072247460E+06]  # [km]
t         = 5*24*60*60                                                            # [s]
Mu        = 1.327e+11                                                             # [km^3/s^2]
Tolerance = 0.00001
MaxInt    = 10000
options   = 'vector'

 # check if supplied vectors are a list or a numpy array, convert to numpy array if not
if isinstance(r1, np.ndarray)   == True:
    pass
elif isinstance(r1, np.ndarray) == False:
    r1 = np.asarray(r1)
else:
    raise BAD_INPUT
        
if isinstance(r2, np.ndarray)   == True:
    pass
elif isinstance(r2, np.ndarray) == False:
    r2 = np.asarray(r2)
else:
    raise BAD_INPUT

 # Find the chord length between the two positions
if options == 'vector':
    c     = norm(r2 - r1) # vector subtraction
elif options == 'magnitude':
    theta = np.arccos((np.dot(r1,r2))/(norm(r1) * norm(r2))) # angle between two vectors
    c     = np.sqrt(r1**2 + r2**2 - 2*r1*r2*np.cos(theta))   # law of cosines
else:
    raise BAD_INPUT
        
# Find semi-perimeter 
s = (c + norm(r1) + norm(r2))/2;

# need an initial guess for a and delta T
a_min = s/2
a_max = 2*s
a     = (a_min + a_max)/2
alpha = (np.arcsin(np.sqrt((s)/(2*a))))   * 2
beta  = (np.arcsin(np.sqrt((s-c)/(2*a)))) * 2
g     = np.sqrt((a**3)/(Mu)) * (alpha - beta - (np.sin(alpha) - np.sin(beta)))

# create iteration counter
i = 1

# Use bisection method to solve lameberts problem for semi major axis
while(np.abs(t-norm(g)) > Tolerance):
    i     = i+1
    a     = (a_min + a_max)/2
    alpha = (np.arcsin(np.sqrt((s)/(2*a)))) * 2
    beta  = (np.arcsin(np.sqrt((s-c)/(2*a)))) * 2
    g     = np.sqrt((a**3)/(Mu)) * (alpha - beta - (np.sin(alpha) - np.sin(beta)))
 
    # bisection method
    if norm(g) > t:
        a_min = a
    elif norm(g) < t:
        a_max = a
 
    if i > MaxInt:
        raise MAX_ITERATIONS_REACHED
        
# Find velocity at positions one and position two 
cotangent1 = 1 / np.tan(alpha/2)
cotangent2 = 1 / np.tan(beta/2)
A  = (np.sqrt(Mu/(4*a))) * cotangent1
B  = (np.sqrt(Mu/(4*a))) * cotangent2

u1 = (r1) / (norm(r1))
u2 = (r2) / (norm(r2))
uc = (r2 - r1)/c

v1 = ((B+A)*uc) + ((B-A)*u1)
v2 = ((B+A)*uc) - ((B-A)*u2)


print(a)
print(v1)
print(v2)
