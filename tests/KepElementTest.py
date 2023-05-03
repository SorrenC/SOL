# imports 
import sys
import numpy as np
sys.path += ['C:/Users/sorre/Desktop/Programs/SOL/src/Functions',
            'C:/Users/sorre/Desktop/Programs/SOL/src/Constants']

from KepElements import KepElements
from PlanetConsts import SUN_MU
from scipy.linalg import norm 

# Test to ensure that functions are accurate and working corrctly

# State vectors from Sun body center to Mars J2000 2022-Sep-30 00:00:00 TDB. From JPL's horizon system
#r  =  np.array([1.705762706464142E+08 , 1.331457466962230E+08 ,-1.393668994909272E+06])
#v  =  np.array([-1.398483275256669E+01,2.117008216903941E+01  ,7.867324973063816E-01])

r  =  np.array([-1.666285496079473E+08,1.832649379659352E+08,7.929803072247460E+06])
v  =  np.array([-17.07976786,-14.17071434,0.12240516])
Mu =  SUN_MU

d     = KepElements(r,v,Mu)
eccen = d.Eccentricity()
inc   = d.inclination()
a     = d.SemiMajorAxis()
Raan  = d.RAAN()
Aop   = d.AOP()
TrAnm = d.TrueAnomaly()
All   = d.SolveAll()

print("Eccentricity:         %.3f    " %norm(eccen))
print("Orbital Inclination:  %.3f deg" %inc)
print("SemiMajor Axis:       %.3f km"  %norm(a))
print("R.A.A.N:              %.3f deg" %Raan)
print("Argument of Peripsis  %.3f deg" %Aop)
print("True Anomaly:         %.3f deg" %TrAnm)