import sys
sys.path.append("C:/Users/sorre/Desktop/Programs/SOL/src/")

from KepElements import *

# Test to ensure that functions are accurate and working corrctly

# State vectors from sun to Mars
r  = [1.692167431596910e+08,1.332858910440899e+08,-1.363164898702294e+06]
v  = [-1.398517076752354e+01, 2.115435793447175e+01, 7.868656661555926e-01]
Mu = 132700000000

d     = KepElements(r,v,Mu)
eccen = d.Eccentricity()
inc   = d.inclination()
a     = d.SemiMjAxis()
Raan  = d.RAAN()
Aop   = d.AOP()
TrAnm = d.TrueAnmly()

print("Eccentricity:        %.3f" % norm(eccen))
print("Orbital Inclination: %.3f deg" %inc)
print("SemiMajor Axis:      %.3f km" %norm(a))
print("R.A.A.N:             %.3f" %Raan)
print("Argument of Perigee  %.3f" %Aop)
print("True Anomaly:        %.3f deg" %TrAnm)