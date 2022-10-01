import sys
sys.path.append("C:/Users/sorre/Desktop/Programs/SOL/src/Functions")

from KepElements import *

# Test to ensure that functions are accurate and working corrctly

# State vectors from Sun body center to the Earth. From JPL's horizon system
r  =  [1.488800356776601e+08 , 1.699418513335430e+07 ,-1.583093478363939e+03]
v  =  [-3.872589829328815e+00 , 2.949064770350737e+01 ,-3.733711422633235e-04]
Mu = 1.327e+11

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