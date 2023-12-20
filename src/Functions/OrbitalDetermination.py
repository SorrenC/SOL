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
# Determines an orbit based on observational measurments. Uses Gauss's and laplace methods of orbital
# determination to uniquely fit an orbit based on observational data and outputs the six keplerian 
# orbital elements to describe the orbit. Requires knowledge of the central body the object is orbiting.
# Requires three measurments 
#
# INPUTS:
#   t1 = time at observation 1
#   t2 = time at observation 2
#   t3 = time at observation 3
#
# OUTPUTS:
#   
#########################################################################################################

# Imports
import numpy as np
import scipy as sci
import math  as m 