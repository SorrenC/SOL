#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    05/3/2023
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## OrbitalPropagation ###########################################
#
# Propogates an oribit forward in time of an orbiting body around some central body given a known positon
# vector and velocity vector at some initial time t0 and a desired delta t, that is, how much forward in 
# time the user desires to propagate the orbit
#
# INPUTS:
#   r1        = position 1 in vector or magnitude. Either python list or numpy array 
#   v2        = velocity 1 in vector or magnitude. Either python list or numpy array
#   dt        = amount of time forward to propagate orbit
#   Mu        = central body orbital parameter 
#   Tolerance = stopping condition for numerical method
#   MaxInt    = maximum iterations before algorithm stops 
#   option    = used to indicate in position given as vector or magnitude 
#
# OUTPUTS:
#   f         = True anamoly of new position in orbit after dt from inital position
#   v1        = velocity vector at position 1 
#   v2        = velocity vector at position 2
#   
#########################################################################################################

# imports
import math  as m 
import numpy as np
from numpy.linalg import norm 
from Exceptions   import *

