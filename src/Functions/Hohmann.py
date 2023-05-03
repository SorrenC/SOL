#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    10/5/2022
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## Hohmann ######################################################
#
# Module to calcualte delta V requrments for a variety of Hohmann transfer cases
#
#########################################################################################################

# r1 - initial circular orbit 
# r2 - desired circular orbit
# Mu - gravitation parameter of attracting body

# imports 
import numpy as np

class Hohmann():

    def __init__(self,r1,r2,Mu):
        self.r1 = r1
        self.r2 = r2
        self.Mu = Mu

    def Circular(self):
        dV1   = np.sqrt(self.Mu/self.r1) * (np.sqrt((2*self.r2)/(self.r1+self.r2)) - 1)
        dV2   = np.sqrt(self.Mu/self.r2) * (1 - np.sqrt((2*self.r1)/(self.r1+self.r2)))
        dVtot = dV1 + dV2
        Tof   = np.pi * (np.sqrt(((self.r1+self.r2)**3)/(8*self.Mu)))
        return np.array([dV1,dV2,dVtot,Tof])