# Test/Example of how to use the Hohmann transfer orbit module 

import sys
import os 

# Add the project root to sys.path and also put path at top of list so python searches this path first
rootpath = sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
if rootpath not in sys.path:
    sys.path.insert(0,rootpath)

import numpy as np
from src.Functions.Hohmann import Hohmann
from src.Functions.PlanetConsts import EARTH_MU
from src.Functions.PlanetConsts import EARTH_RADIUS


# Go from a circular orbit to another circualr orbit around Earth
# R1 and R2 must be given as the orbital radius from the center of the body, NOT ALTITUDE!
# If you problem specifies an initial and final orbit by altitude you MUST add the radius of the earth to that value i.e 300 km + EARTH_RADIUS

# Example
r1       = 6700         # [km]
r2       = 93800        # [km]
Mu_earth = EARTH_MU     # [km^3 / s^2]

Hohmann = Hohmann(r1,r2,Mu_earth)
results = Hohmann.Circular()

print("Delta V1:       %.3f km/s" %results[0])
print("Delta V2:       %.3f km/s" %results[1])
print("Total Delta V:  %.3f km/s" %results[2])
print("Time of Fligth: %.3f s"    %results[3])

