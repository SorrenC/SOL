# imports 
import sys
sys.path += ['C:/Users/sorre/Desktop/Programs/SOL/src/Functions',
            'C:/Users/sorre/Desktop/Programs/SOL/src/Constants']
import numpy as np
from KepElements import KepElements
from PlanetConsts import SUN_MU
from scipy.linalg import norm 
from math import sqrt


# Test to ensure that functions are accurate and working corrctly

# State vectors from Sun body center to Mars J2000 2022-Sep-30 00:00:00 TDB. From JPL's horizon system
#r  =  np.array([1.705762706464142E+08 , 1.331457466962230E+08 ,-1.393668994909272E+06])
#v  =  np.array([-1.398483275256669E+01,2.117008216903941E+01  ,7.867324973063816E-01])

# State vectors from Solar System barycenter to Mars. From JPL's horizon system. Coordinate System: J2000 Ecliptic
r  =  np.array([-1.591163034225527E+08,1.892356715610578E+08,7.870476085229695E+06])
v  =  np.array([-17.6949825,-13.46716982,0.15224672])
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


#(self,J2,R,a,e,i):
J2 = 1082.63e-6
Re = 6378.1363
a  = 7000
e  = 0.001
i  = np.radians(98)

RaanJ2 = d.RaanJ2(J2,Re,a,e,i)
print(RaanJ2)