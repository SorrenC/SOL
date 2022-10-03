import sys
import math as m
sys.path.append("C:/Users/sorre/Desktop/Programs/SOL/src/Functions")

from LambertsSolver import *


# Example of using the lamberts solver function to obtain state vectors v1 and v2 from intial 
# position vectors r1 and r2 and then using said vecloity state vectors in conjunction with 
# the position state vectors to calculate the orbital elements of the orbit. 

# This example is the position of the Earth from the sun body center taken 1 full day apart
r1        = np.array([1.488800356776601e+08,1.699418513335430e+07,-1.583093478363939e+03])  # [km]
r2        = np.array([1.485234755617680e+08,1.953943429969961e+07,-1.618889928234741e+03])   # [km]
t         = 24*60*60           # [s]
Mu        = 1.327e+11          # [km^3/s^2]
Tolerance = 0.0001
MaxInt    = 5000


d = LambertsSolver(r1,r2,t,Mu,Tolerance,MaxInt,'vector')
a = d.solve()

print("Semi Major Axis: %.3f km"%a[1])