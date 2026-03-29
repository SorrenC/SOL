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
# time the user desires to propagate the orbit. This function depends on other SolPy functions such as 
# KepElements. 
# NOTE: This function assumes the position and velocity vectors at position are in ECI coordinates
# This orbital propagator was designed to be used in the contex of Keplerian orbits and the classical
# orbital elements, so it is not designed to be used in the context of non-Keplerian orbits such as those
# with significant perturbations. WILL DEVELOP RK4 ORBIT PROPAGATOR IN FUTURE UPDATE.
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
#   r2        = position vector at position 2 
#   v2        = velocity vector at position 2
#   
#########################################################################################################

# imports
import math  as m 
import numpy as np
from KepElements  import KepElements
from numpy.linalg import norm 
from Utilities.Utilities import Array

class KeplerOrbitalPropagator():

    def __init__(self, r1: Array, v1: Array, dt: float, Mu: float, Tolerance: float, MaxInt: int, option: str):
        self.r1        = r1 
        self.v1        = v1 
        self.dt        = dt 
        self.Mu        = Mu 
        self.Tolerance = Tolerance
        self.MaxInt    = MaxInt 
        self.option    = option

        COEs = KepElements(self.r1,self.v1,self.Mu) # find classical orbital elements from intial position and veloicity vectors
        a    = COEs.SemiMajorAxis()
        e    = COEs.EccentricityMag()
        i    = COEs.Inclination()
        W    = COEs.RAAN()
        w    = COEs.AOP()
        f    = COEs.TrueAnomaly()
        


r  = [-1.591163034225527E+08,1.892356715610578E+08,7.870476085229695E+06]  
v  = [-17.6949825,-13.46716982,0.15224672]

obj = KeplerOrbitalPropagator(r,v,5*24*60*60,SUN.mu,0.0001,10000,'vector')