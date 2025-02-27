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

    def __init__(self,Inclination,SemiMajorAxis,Eccentricity,Raan,Aop,TrueAnomaly):

        self.i = Inclination # Orbital Inclination [deg]
        self.a = SemiMajorAxis # Semi major axis [km]
        self.e = Eccentricity # Orbital eccentricity [dimensionless]
        self.W = Raan # Right asscension of ascending node [deg]
        self.w = Aop # Argument of periapsis [deg]
        self.f = TrueAnomaly # True anomaly [deg]

    # Convert orbtial elements in Euler angles to ECI coordinates 
    def KepRotation(self):

        # convert degrees to rad
        i = np.radians(self.i)
        W = np.radians(self.W)
        w = np.radians(self.w)

        # Rotation matrix from perifocal (orbital) coordinates to equitorial coordinates
        R = np.array([[(cos(W)*cos(w))-(sin(W)*sin(w)*cos(i)), (-cos(W)*sin(w))-(sin(W)*sin(w)*cos(i)), sin(W)*sin(i)],
                [(sin(W)*cos(w))+(cos(W)*sin(w)*cos(i)), (-sin(W)*sin(w))+(cos(W)*cos(w)*cos(i)), -cos(W)*sin(i)],
                [(sin(i)*sin(w)), (sin(i)*cos(w)), cos(i)]])
        
        # Need values of all true anomalies to trace out the orbit. Create 1000 evenly space points between 0 and 2*pi i.e a full orbit
        f_range = np.linspace(0,2*np.pi,1000)

        # Find orbital radius in the orbital plane for each value of true anomaly
        radius = ((self.a*(1-self.e**2))/(1+(self.e*cos(f_range))))

        # Find position in orbital plane
        x = radius*sin(f_range)
        y = radius*cos(f_range)

        # Perform matrix multiplication to transform perifocal frame to equitorial frame
        equitorial_orbit_3D = np.dot(R, np.vstack((x, y, np.zeros_like(x))))

        return equitorial_orbit_3D
    
    # Function to plot orbit in equitorial frame from keplerian orbital elements
    def KepPlot(self):

        Orbit = self.KepRotation()

        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(111,projection='3d')

        ax.plot(Orbit[0],Orbit[1],Orbit[2],label='Orbit Path',color='b')
        ax.scatter([0],[0],[0],color='yellow',s=200,label='Central Body')

        ax.set_xlabel("X (km)")
        ax.set_ylabel("Y (km)")
        ax.set_zlabel("Z (km)")
        ax.set_title("3D Orbit Plot")
    
        ## NEED TO FIGURE OUT BETTER WAY TO AUTOMATICALLY SET AXES SCALE SO PLOT IS NOT STRETCHED
        ax.set_zlim([-8e10,6e10])
        #ax.set_xlim([-10e8,10e8])
        #ax.set_ylim([-4e8,4e8])

        ax.view_init(elev=30,azim=45)  # Adjust elevation and azimuth as needed

        ax.legend()
        plt.show()


e=0   
i=0
a=229424967.891
W=0
w=0
f=150.814 

Plot = KepElementPlot(i,a,e,W,w,f)
Plot.KepPlot()