#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    12/23/2023
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## Bi Elliptic Transfer #########################################
#
# Module to calcualte delta V requrments and time of flights for a variety of bi elliptic transfer cases. 
#
#########################################################################################################

import numpy as np
import math  as m 
import matplotlib.pyplot as plt

class BiElliptic():

    def Circular(Mu,Ri,Rf,Rb):
        # Circular
        #
        # Inputs: 
        #       Ri = initial circular radius around central body (km)
        #       Rf = final circular radius around central body  (km)
        #       Rb = user specified transfer ellipse radius. Rb > R1 & R2 (km)
        #
        # Outputs:
        #       dV1   = delta v required for first burn to put into transfer ellipse (km/s)
        #       dV2   = delta v required for second burn to decrease orbital radius to desired distance (km/s)
        #       dV3   = delta v requiref for third burn to circularize orbit (km/s)
        #       dVtot = Total delta v (km/s)
        #       t1    = r1 to rb transfer time (s)
        #       t2    = rb to r2 transfer time (s)
        #       t     = total transfer time (s)

        # Assumptions:
        #       Transfer between circular orbits with impulsive manuevers i.e burn time << time of flight 
        #
        #


        # Calcualte semi-major axes 
        a1 = (Ri+Rb)/2
        a2 = (Rf+Rb)/2
        
        # Calcuate delta v changes 
        dV1   = np.sqrt((2*Mu)*(Rb/(Ri*(Ri+Rb)))) - np.sqrt(Mu/Ri)                        # dV1 = V1,p - Vi
        dV2   = np.sqrt((2*Mu)*(Rf/(Rb*(Rf+Rb)))) - np.sqrt((2*Mu)*(Ri/(Rb*(Ri+Rb))))     # dV2 = V2,a - V1,a
        dV3   = np.sqrt(Mu/Rf) - np.sqrt((2*Mu)*(Rb/(Rf*(Rf+Rb))))                        # dV3 = Vf - V2,p
        dVtot = np.abs(dV1) + np.abs(dV2) + np.abs(dV3)   # Take absolute value of each dV because we know sign +/- will indicate direction of thrust (prograde or retrograde) will be different but we want total delta V                                                  

        # Calculate times transfer times
        t1  = m.pi * np.sqrt(((a1)**3)/(Mu))
        t2  = m.pi * np.sqrt(((a2)**3)/(Mu))
        t   = t1 + t2

        return np.array([dV1,dV2,dV3,dVtot,t1,t2,t])
    
    def Plot(Ri,Rf,Rb):
        
        center_x = 0
        center_y = 0

        theta = np.linspace(0, 2*np.pi, 100)
        theta2 = np.linspace(0,2*np.pi,100)

        # Calculate ellipse points for Ri
        xi = Ri * np.cos(theta) + center_x
        yi = Ri * np.sin(theta) + center_y

        # Calculate ellipse points for Rf
        xf = Rf * np.cos(theta) + center_x
        yf = Rf * np.sin(theta) + center_y

        # Calculate ellipse points for Rb
        xb = Rb * np.cos(theta2) + center_x
        yb = Rb * np.sin(theta2) + center_y

        # Plot the ellipse
        plt.figure(figsize=(8, 6))
        plt.plot(yi,xi)
        plt.plot(yf,xf)
        plt.plot(yb,xb)
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("2D Orbital Ellipse")
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box') # Ensure equal aspect ratio
        plt.show()