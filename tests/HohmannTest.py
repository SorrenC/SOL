# Test/Example of how to use the Hohmann transfer orbit module 

import sys
import numpy as np
sys.path += ['C:/Users/sorre/Desktop/Programs/SOL/src/Functions',
            'C:/Users/sorre/Desktop/Programs/SOL/src/Constants']
from Hohmann import *
from PlanetConsts import EARTH_MU
from PlanetConsts import EARTH_RADIUS


# Go from a circular orbit to another circualr orbit around Earth
# R1 and R2 must be given as the orbital radius from the center of the body, NOT ALTITUDE!

# Example, altitude of 300 km to 800 km around Earth
r1       = 300 + EARTH_RADIUS   # [km]
r2       = 800 + EARTH_RADIUS   # [km]
Mu_earth = EARTH_MU             # [km^3 / s^2]

Hohmann = Hohmann(r1,r2,Mu_earth)
results = Hohmann.Circular()

print("Delta V1:       %.3f km/s" %results[0])
print("Delta V2:       %.3f km/s" %results[1])
print("Total Delta V:  %.3f km/s" %results[2])
print("Time of Fligth: %.3f s"    %results[3])

