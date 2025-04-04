# Test/Examples of how to use the BiElliptic transfer orbit module 

import sys
import numpy as np
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/functions'))) # relative import
from BiElliptic import *
from PlanetConsts import EARTH_MU


# Go from a circular orbit to another circualr orbit around Earth
# R1 and R2 must be given as the orbital radius from the center of the body, NOT ALTITUDE!
# If you problem specifies an initial and final orbit by altitude you MUST add the radius of the earth to that value i.e 300 km + EARTH_RADIUS

# Example
# Test case : Object in low earth orbit to high earth orbit. Test case presented in wikipedia article for bi-elliptic transfers
Mu = EARTH_MU
Ri = 6700
Rf = 93800
Rb = 40*(Ri)

answer = np.abs(BiElliptic.Circular(Mu,Ri,Rf,Rb))
print("Delta V1:       %.5f km/s" %answer[0])
print("Delta V2:       %.5f km/s" %answer[1])
print("Delta V3:       %.5f km/s" %answer[2])
print("Total Delta V:  %.5f km/s" %answer[3])
print("Time of Fligth: %.5f s"    %answer[6])

BiElliptic.Plot(Ri,Rf,Rb)

