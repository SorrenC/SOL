###########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    02/25/2025
# Contact: sorrenchandra@gmail.com
#
###########################################################################################################

########################################## Keplerian Element Plot #########################################
#
# Creates a 3D plot given the six keplerian orbital elements input and information about the body being
# oribted. Tjs plotter assumed a keplerian orbital element that is not hyperbolic i.e e<1. Inputs NEED to
# be in degrees, the function will convert them to radians
#
# INPUTS:
#   i      = orbital inclination (rad)
#   a      = semi-major axis (km)
#   e      = orbital eccentricity (dimensionless)
#   RAAN   = right asscension of ascending node (deg)
#   AOP    = argument of periapsis (deg)
#   Nu     = true anomaly (deg)
#   R_body = radius of larger body (km)
#
# OUTPUTS:
#  
#   
#########################################################################################################

### IMPORTS ####
import numpy as np
import math as m
import matplotlib.pyplot as plt
from numpy import sin as sin 
from numpy import cos as cos

### CLASS DEFINITIONS ###
class KepElementPlot():
    
    # Class variables
    def __init__(self,i,a,e,W,w,f):
        self.i = i # orbital inclination
        self.a = a # semi major axis
        self.e = e # orbital eccentricity
        self.W = W # Right asscension of ascending node
        self.w = w # argument of periapsis
        self.f = f # true anomaly 

    # Convert orbtial elements in Euler angles to ECI coordinates 
    def KepRoataion():

        # convert degrees to rad
        i = np.radians(i)
        W = np.radians(W)
        w = np.radians(w)
        f = np.radians(f)

        # Rotation matrix from perifocal coordinates to equitorial coordinates
        r = np.array([(cos(W)*cos(w))-(sin(W)*sin(w)*cos(i)), (-cos(W)*sin(w))-(sin(W)*sin(w)*cos(i)), sin(W)*sin(i)],
                     [(sin(W)*cos(w))+(cos(W)*sin(w)*cos(i)), (-sin(W)*sin(w))+(cos(W)*cos(w)*cos(i)), -cos(W)*sin(i)],
                     [(sin(i)*sin(w)), (sin(i)*cos(w)), cos(i)])
