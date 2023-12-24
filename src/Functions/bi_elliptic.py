#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    10/5/2022
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

class BiElliptic():

    def Circular(Mu,Ri,Rf,Rb):
        # Circular
        #
        # Inputs: 
        #       Ri = initial circular radius around central body (km)
        #       Rf = final circular radius around central8 body  (km)
        #       Rb = user specified transfer ellipse radius. Rb > R1 & R2 (km)
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

        # Calcualte semi-major axes 
        a1 = (Ri+Rb)/2
        a2 = (Rf+Rb)/2
        
        # Calcuate delta v changes 
        dV1   = np.sqrt((2*Mu)*(Rb/(Ri*(Ri+Rb)))) - np.sqrt(Mu/Ri)                        # dV1 = V1,p - Vi
        dV2   = np.sqrt((2*Mu)*(Rf/(Rb*(Rf+Rb)))) - np.sqrt((2*Mu)*(Ri/(Rb*(Ri+Rb))))     # dV2 = V2,a - V1,a
        dV3   = np.sqrt(Mu/Rf) - np.sqrt((2*Mu)*(Rb/(Rf*(Rf+Rb))))                        # dV3 = Vf - V2,p
        dVtot = dV1 + dV2 + dV3                                                  

        # Calculate times transfer times
        t1  = m.pi * np.sqrt(((a1)**3)/(Mu))
        t2  = m.pi * np.sqrt(((a2)**3)/(Mu))
        t   = t1 + t2

        return np.array([dV1,dV2,dV3,dVtot,t1,t2,t])

# Test case : Earth to Uranus assuming both planet orbits are circular (they are not). Taking semi major axis of each orbit as orbital radius 
Mu = 1.327e+11
Ri = 149.598e+6
Rf = 2867.043e+6
Rb = 1.5*(Rf)

answer = np.abs(BiElliptic.Circular(Mu,Ri,Rf,Rb))
print(answer)

