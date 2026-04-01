# imports 
import numpy as np
import math as m
from numpy.linalg import norm
from sol.Functions.OrbitDetermination.KepElements import KepElements
from sol.Functions.Constants.PlanetConsts import SUN, EARTH

# Test to ensure that functions are accurate and working corrctly

# State vectors from Solar System barycenter to Mars. From JPL's horizon system. Coordinate System: J2000 Ecliptic. GOOD RESULTS
r  =  np.array([-1.591163034225527E+08,1.892356715610578E+08,7.870476085229695E+06])
v  =  np.array([-17.6949825,-13.46716982,0.15224672])


# GOES 18 geostationary satellite March 15 2026 00:00:0000
r  = np.array([3.454231365705961E+04,2.213689762733308E+04,-9.711965558423912E+03])  
v  = np.array([-1.763149711502538E+00,2.313401149735242E+00,-9.973972570908335E-01])

# Chandra X-Ray observatory March 15 2026 00:00:0000
r = np.array([2.911759704720346E+04,-4.300993229313808E+04,1.346969977868364E+04])
v = np.array([-4.023444582553123E-01,1.983103046313508E+00,-2.414844639225887E+00])

d     = KepElements(r,v,EARTH.mu)
eccen = d.Eccentricity()
inc   = d.inclination()
a     = d.SemiMajorAxis()
Raan  = d.RAAN()
Aop   = d.AOP()
TrAnm = d.TrueAnomaly()
All   = d.SolveAll()

print("Eccentricity:         %.3f    " %norm(eccen))
print("Orbital Inclination:  %.3f deg" %m.degrees(inc))
print("SemiMajor Axis:       %.3f km"  %a)
print("R.A.A.N:              %.3f deg" %Raan)
print("Argument of Peripsis  %.3f deg" %Aop)
print("True Anomaly:         %.3f deg" %TrAnm)