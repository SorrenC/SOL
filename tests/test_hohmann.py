# Test/Example of how to use the Hohmann transfer orbit module 

# Imports
from sol.Functions.Maneuvers.Hohmann import Hohmann
from sol.Functions.Constants.PlanetConsts import EARTH

# Go from a circular orbit to another circualr orbit around Earth
# R1 and R2 must be given as the orbital radius from the center of the body, NOT ALTITUDE!
# If you problem specifies an initial and final orbit by altitude you MUST add the radius of the earth to that value i.e 300 km + EARTH_RADIUS

# Example
r1       = 6700.0         # [km]
r2       = 93800.0        # [km]
Mu_earth = EARTH.mu     # [km^3 / s^2]

Hohmann = Hohmann(r1,r2,Mu_earth)
results = Hohmann.Circular()

print("Delta V1:       %.3f km/s" %results[0])
print("Delta V2:       %.3f km/s" %results[1])
print("Total Delta V:  %.3f km/s" %results[2])
print("Time of Fligth: %.3f s"    %results[3])

