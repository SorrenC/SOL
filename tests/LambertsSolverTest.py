import sys
import math as m
sys.path.append("C:/Users/sorre/Desktop/Programs/SOL/src/Functions")

from LambertsSolver import *
from KepElements import *

# Example of using the lamberts solver function to obtain state vectors v1 and v2 from intial 
# position vectors r1 and r2 and then using said vecloity state vectors in conjunction with 
# the position state vectors to calculate the orbital elements of the orbit. 

############################ VECTOR EXAMPLE ####################################################################################
# This example is the position of Mars from the sun body center taken 1 full day apart
r1_vector = np.array([1.705762706464142E+08,1.331457466962230E+08,-1.393668994909272E+06])  # [km]
r2_vector = np.array([1.693596693212054E+08,1.349683079588937E+08,-1.325628359792881E+06])   # [km]
t         = 24*60*60           # [s]
Mu        = 1.327e+11          # [km^3/s^2]
Tolerance = 0.0001
MaxInt    = 5000


vec_solution=LambertsSolver(r1_vector,r2_vector,t,Mu,Tolerance,MaxInt,'vector')
solution= vec_solution.solve()
print("Semi Major Axis: %.3f km" %solution[0][0])

# Now use known postion vector 1 of Mars and the calcualted velocity vector at point 1 to calcualte Mars orbital elements


############################ MAGNITUDE EXAMPLE ####################################################################################

