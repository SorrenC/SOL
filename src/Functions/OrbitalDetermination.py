#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    12/19/2023
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## OrbitalDetermination #########################################
#
# Determines an orbit based on observational measurments. Uses Gauss's methods of orbital
# determination to uniquely fit an orbit based on observational data and outputs the six keplerian 
# orbital elements to describe the orbit. Requires knowledge of the central body the object is orbiting.
# Requires three observational measurments 
#
# INPUTS:
#   rho1 = Observation 1 from point of observation 
#   rho2 = Observation 2 from point of observation 
#   rho3 = Observation 3 from point of observation 
#   R_og = Position from center of mass to point of observation (Radius of earth for geocentric orbits)
#   t1   = time at observation 1
#   t2   = time at observation 2
#   t3   = time at observation 3
#   Mu   = Gravitaional paramater of the central body 
#
# OUTPUTS:
#   r1   =
#   r2   =
#   r3   =
#   
#########################################################################################################

# Imports
import numpy as np
import scipy as sci
import math  as m 

class OrbitDetermine():
    
    def __init__(self,rho1,rho2,rho3,t1,t2,t3,R_og,Mu);
        self.rho1 = rho1
        self.rho2 = rho2
        self.rho3 = rho3
        self.R_og = R_og
        self.t1   = t1
        self.t2   = t2
        self.t3   = t3
        self.Mu   = Mu

