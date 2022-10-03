import sys
sys.path += ['C:/Users/sorre/Desktop/Programs/SOL/src/Functions',
            'C:/Users/sorre/Desktop/Programs/SOL/src/Constants']

from KepElements import KepElements
from PlanetConsts import SUN_MU
from scipy.linalg import norm 

# Test to ensure that functions are accurate and working corrctly

# State vectors from Sun body center to Mars 2022-Sep-30 00:00:00 TDB. From JPL's horizon system
r  =  [1.705762706464142E+08 , 1.331457466962230E+08 ,-1.393668994909272E+06]
v  =  [-1.398483275256669E+01,2.117008216903941E+01  ,7.867324973063816E-01]
Mu =  SUN_MU

d     = KepElements(r,v,Mu)
eccen = d.Eccentricity()
inc   = d.inclination()
a     = d.SemiMajorAxis()
Raan  = d.RAAN()
Aop   = d.AOP()
TrAnm = d.TrueAnmly()

print("Eccentricity:         %.3f    " %norm(eccen))
print("Orbital Inclination:  %.3f deg" %inc)
print("SemiMajor Axis:       %.3f km"  %norm(a))
print("R.A.A.N:              %.3f deg" %Raan)
print("Argument of Peripsis  %.3f deg" %Aop)
print("True Anomaly:         %.3f deg" %TrAnm)