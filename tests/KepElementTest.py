# imports 
import sys
import os 
import numpy as np

# Add the project root to sys.path and also put path at top of list so python searches this path first
rootpath = sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
if rootpath not in sys.path:
    sys.path.insert(0,rootpath)

from numpy.linalg import norm
from src.Functions.KepElements import KepElements
from src.Functions.PlanetConsts import SUN

# Test to ensure that functions are accurate and working corrctly

# State vectors from Solar System barycenter to Mars. From JPL's horizon system. Coordinate System: J2000 Ecliptic
r  =  np.array([-1.591163034225527E+08,1.892356715610578E+08,7.870476085229695E+06])
v  =  np.array([-17.6949825,-13.46716982,0.15224672])
Mu =  SUN.mu

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
print("SemiMajor Axis:       %.3f km"  %a)
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