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
# Module to calcualte delta V requrments for a variety of bi elliptic transfer cases. 
#
#########################################################################################################

import numpy as np
import math  as m 

class BiElliptic():
    
    # Circular
    #
    # Inputs: 
    #       r1 = initial circular radius around central body
    #       r2 = final circular radius around central body 
    #       rb = user specified transfer ellipse radius. rb should be greater than r1 and r2
    # Outputs:
    #       dV1 = delta v required for first burn to put into transfer ellipse
    #       dV2 = delta v required for second burn to decrease orbital radius to desired distance
    #       dV3 = delta v requiref for third burn to circularize orbit
    #       t1  = r1 to rb transfer time
    #       t2  = rb to r2 transfer time 
    #       t   = total transfer time
     
    def Circular(Mu,r1,r2,rb):

        # since circular orbit, the radius and semimajor axis are the same
        a1 = r1
        a2 = r2
        
        dV1 = np.sqrt(((2*Mu)/r1) - (Mu/a1)) - np.sqrt(Mu/r1)
        dV2 = np.sqrt(((2*Mu)/rb) - (Mu/a2)) - np.sqrt(((2*Mu)/rb) - (Mu/a1)) 
        dV3 = np.sqrt(((2*Mu)/r2) - (Mu/a2)) - np.sqrt(Mu/r2)

        t1  = m.pi * np.sqrt(((a1^2)/2)/Mu)
        t2  = m.pi * np.sqrt(((a2^2)/2)/Mu)
        t   = t1 + t2
        return np.array([dV1,dV2,dV3,t1,t2,t])

Mu = 3.986e+5
r1 = 500+6873
r2 = 1000+6873
rb = 1500+6873

answer = BiElliptic.Circular(Mu,r1,r2,rb)
print(answer)

