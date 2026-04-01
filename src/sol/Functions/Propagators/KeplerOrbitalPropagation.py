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
#
# This function assumes the position and velocity vectors at position are in ECI coordinates
# This orbital propagator was designed to be used in the contex of Keplerian orbits and the classical
# orbital elements so 0 < e < 1. This function solves keplers equation using a numerical method to 
# determine ecentric anomaly which is then used to determine a new true anomaly. From there a new 
# position and velocity vector are determined. 
#  
# INPUTS:
#   r1        = position 1 in vector or magnitude. Either python list or numpy array 
#   v2        = velocity 1 in vector or magnitude. Either python list or numpy array
#   dt        = amount of time forward to propagate orbit in seconds 
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

# Standard Library Imports
import math as m

# 3rd Party Imports
from numpy.linalg import norm
import numpy as np

# SOL Library Imports
from sol.Functions.OrbitDetermination.KepElements import KepElements
from sol.Functions.Utils.Utilities import Array
from sol.Functions.Constants.PlanetConsts import SUN, EARTH

class KeplerOrbitalPropagator():

    def __init__(self, r1: Array, v1: Array, dt: float, Mu: float, Tolerance: float, MaxInt: int, option: str) -> None: 
        self.r1        = r1 
        self.v1        = v1 
        self.dt        = dt 
        self.Mu        = Mu 
        self.Tolerance = Tolerance
        self.MaxInt    = MaxInt 
        self.option    = option

    def NewtonRaphsonSolver(self) -> float:

        COEs = KepElements(self.r1,self.v1,self.Mu)              # find classical orbital elements from intial position and veloicity vectors,

        # Only need semi major axis and eccentricity to solve for mean motion
        a   = COEs.SemiMajorAxis()                               # semi major axis
        e   = norm(COEs.Eccentricity())                          # eccentricity vector normalized
        f0   = m.radians(COEs.TrueAnomaly())                     # true anomaly at initial point converted to radians
        
        # find mean anomaly and eccentric anomlay of orbit
        E0  = m.atan2(m.sqrt(1-e**2)*m.sin(f0), e + m.cos(f0))   ### REWRITE
        M0  = E0 - e*m.sin(E0)                                   # Mean anomaly at initial point
        n   = m.sqrt(self.Mu/(a**3))                             # mean motion
        M   = M0+n*self.dt                                       # mean anomaly [rads]
        Ek  = M                                                  # set eccentric anomaly to mean anomaly for an intial guess 
        

        delta = (M - Ek + e*m.sin(Ek)) / (e*m.cos(Ek) - 1)
        Ek = Ek - delta
        # Use newton raphson method to solve for eccentric anomaly
        i = 0                                                    # iteration counter
        while (abs(delta) > self.Tolerance):

            Ek = Ek - ((M-Ek+e*m.sin(Ek)) / (e*m.cos(Ek)-1))

            i += 1 
            if i > self.MaxInt:
                break
      
        print("# of iterations: ",i)
        # final answer
        E = Ek

        f = m.atan2(m.sqrt(1 - e**2) * m.sin(E),m.cos(E) - e)   # use atan2 to resolve quadrant ambiguity 

        if f < 0:             
            f = f + (2*m.pi)                                      # add 2pi to bound our answer between 0 and 2*pi

        print("e   = %.3f" %e)
        print("nu0 = %.3f" %m.degrees(f0))
        print("E0  = %.3f" %E0)
        print("M0  = %.3f" %M0)
        print("M   = %.3f" %M)
        print("E   = %.3f" %E)

        return f    
        


## TEMPORARY TESTING AREA. Will move this to proper test file once I know function works correctly 

# GOES 18 geostationary satellite r and v vecotrs 15 March 2026 00:00:000 GMT from NASA JPL Horizon system
r0 = np.array([2.911759704720346E+04,-4.300993229313808E+04,1.346969977868364E+04])
v0 = np.array([-4.023444582553123E-01,1.983103046313508E+00,-2.414844639225887E+00])
dt = 2*24*60*60

obj = KeplerOrbitalPropagator(r0,v0,dt,EARTH.mu,1e-3,10000,'vector')
ans = obj.NewtonRaphsonSolver()
print("F   = %.3f" %ans,"Rads")
print("F   = %.3f" %m.degrees(ans),"degrees")