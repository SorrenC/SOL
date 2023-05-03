import sys
sys.path += ['C:/Users/sorre/Desktop/Programs/SOL/src/Functions','C:/Users/sorre/Desktop/Programs/SOL/src/Constants']
from LambertsSolver import LambertsSolver
from KepElements import KepElements
from PlanetConsts import SUN_MU


# Example of using the lamberts solver function to obtain state vectors v1 and v2 from intial 
# position vectors r1 and r2 and then using said vecloity state vectors in conjunction with 
# the position state vectors to calculate the orbital elements of the orbit. 

############################ VECTOR EXAMPLE ####################################################################################

# This example is the position of Mars from the sun body center taken 1 full day apart
r1_vector = [1.705762706464142E+08,1.331457466962230E+08,-1.393668994909272E+06]  # [km]
r2_vector = [1.693596693212054E+08,1.349683079588937E+08,-1.325628359792881E+06]  # [km]
t         = 24*60*60                                                              # [s]
Mu        = SUN_MU                                                                # [km^3/s^2]
Tolerance = 0.0001
MaxInt    = 5000


vec_solution=LambertsSolver(r1_vector,r2_vector,t,Mu,Tolerance,MaxInt,'vector')
solution= vec_solution.BiSection()

# Function returns a tuple of numpy arrays, extract data from 'solution'
print(solution[0])
print(solution[1])
print(solution[2])

# Now use known postion vector 1 of Mars and the calcualted velocity vector at point 1 to calcualte Mars orbital elements
#r  =  r1_vector
#v  =  solution[1]
#Mu =  SUN_MU

#d     = KepElements(r,v,Mu)
#eccen = d.Eccentricity()
#inc   = d.inclination()
#a     = d.SemiMajorAxis()
#Raan  = d.RAAN()
#Aop   = d.AOP()
#TrAnm = d.TrueAnomaly()
#All   = d.SolveAll()

#print("Eccentricity:         %.3f    " %norm(eccen))
#print("Orbital Inclination:  %.3f deg" %inc)
#print("SemiMajor Axis:       %.3f km"  %norm(a))
#print("R.A.A.N:              %.3f deg" %Raan)
#print("Argument of Peripsis  %.3f deg" %Aop)
#print("True Anomaly:         %.3f deg" %TrAnm)


############################ MAGNITUDE EXAMPLE ####################################################################################

