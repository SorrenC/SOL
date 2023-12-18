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

r  =  np.array([-7.4445E+07,-2.1231E+08,-2.6124E+06])
v  =  np.array([2.3821E+01,-5.8506E+00,-7.0653E-01])
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