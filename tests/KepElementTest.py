import sys
sys.path.append("C:/Users/sorre/Desktop/Programs/SOL/src/")

from KepElements import *

# Test to ensure that functions are accurate and working corrctly

# State vectors from sun to Mars
r  = [1.705762706464142e+08,1.331457466962230e+08,-1.393668994909272e+06]
v  = [-1.398483275256669e+01 ,2.117008216903941e+01,7.867324973063816e-01]
Mu = 1.327e+11

d     = KepElements(r,v,Mu)
eccen = d.Eccentricity()
inc   = d.inclination()
a     = d.SemiMjAxis()
Raan  = d.RAAN()
Aop   = d.AOP()
TrAnm = d.TrueAnmly()

print("Eccentricity:         %.3f" % norm(eccen))
print("Orbital Inclination:  %.3f deg" %inc)
print("SemiMajor Axis:       %.3f km" %norm(a))
print("R.A.A.N:              %.3f deg" %Raan)
print("Argument of Peripsis  %.3f deg" %Aop)
print("True Anomaly:         %.3f deg" %TrAnm)