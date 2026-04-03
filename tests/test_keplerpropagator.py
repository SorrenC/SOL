import numpy as np
import math as m
from sol.Functions.Propagators.KeplerOrbitalPropagation import KeplerOrbitalPropagator
from sol.Functions.Constants.PlanetConsts import SUN, EARTH

## TEMPORARY TESTING AREA. Will move this to proper test file once I know function works correctly 

# GOES 18 geostationary satellite r and v vecotrs 15 March 2026 00:00:000 GMT from NASA JPL Horizon system
r0 = np.array([2.911759704720346E+04,-4.300993229313808E+04,1.346969977868364E+04])
v0 = np.array([-4.023444582553123E-01,1.983103046313508E+00,-2.414844639225887E+00])
dt = 2*24*60*60

obj = KeplerOrbitalPropagator(r0,v0,dt,EARTH.mu,1e-5,10000,'vector')
ans = obj.BisectionSolver()
#ans = obj.NewtonRaphsonSolver()
print("F   = %.3f" %ans,"Rads")
print("F   = %.3f" %m.degrees(ans),"degrees")