#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    10/2/2022
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## LambertsEqn ##################################################
#
# Solves lamberts problem given two position measurments and the time of flight between said position 
# measurments. The program assumes an elliptical orbit
# The following uses a bi-section method
#
# INPUTS:
#   r1        = position 1 in vector or magnitude
#   r2        = position 2 in vector or magnitude 
#   t         = time between position vectors
#   Mu        = central body orbital parameter 
#   Tolerance = stopping condition for bisection method
#   MaxInt    = maximum iterations before bisection algorithm stops 
#   option    = used to indicate in position given as vector or magnitude 
#
# OUTPUTS:
#   a         = orbit semi major axis
#   v1        = velocity vector at position 1 
#   v2        = velocity vector at position 2
#   
#########################################################################################################

# imports 
import math
import numpy as np
from scipy.linalg import norm 
from Exceptions import *


class LambertsSolver():

    def __init__(self,r1,r2,t,Mu,Tolerance,MaxInt,options):
        self.r1        = r1
        self.r2        = r2
        self.t         = t
        self.Mu        = Mu
        self.Tolerance = Tolerance
        self.MaxInt    = MaxInt
        self.options   = options

    def solve(self):
        
        # Find the chord length between the two positions
        if self.options == 'vector':
            c     = np.abs(self.r2 - self.r1) # vector subtraction
        elif self.options == 'magnitude':
            theta = np.arccos((np.dot(self.r1,self.r2))/(norm(self.r1) * norm(self.r2))) # angle between two vectors
            c     = np.sqrt(self.r1**2 + self.r2**2 - 2*self.r1*self.r2*np.cos(theta))   # law of cosines
        else:
            pass # TO DO: ADD EXCEPTIONS FILE AND CUSTOM EXCEPTIONS

        # Find semi-perimeter 
        s = (c + norm(self.r1) + norm(self.r2))/2;

        # need an initial guess for a and delta T
        a_min = s/2
        a_max = 2*s
        a     = (a_min + a_max)/2
        alpha = np.arcsin(np.sqrt((s)/(2*a))) * 2
        beta  = np.arcsin(np.sqrt((s-c)/(2*a))) * 2
        g     = np.sqrt((a**3)/(self.Mu)) * (alpha - beta - (np.sin(alpha) - np.sin(beta)))

        # create iteration counter
        i = 1

        # Use bisection method to solve lameberts problem for semi major axis
        while(np.abs(self.t-norm(g)) > self.Tolerance):
            i     = i+1
            a     = (a_min + a_max)/2
            alpha = np.arcsin(np.sqrt((s)/(2*a))) * 2
            beta  = np.arcsin(np.sqrt((s-c)/(2*a))) * 2
            g     = np.sqrt((a**3)/(self.Mu)) * (alpha - beta - (np.sin(alpha) - np.sin(beta)))
 
            # bisection method
            if norm(g) > self.t:
                a_min = a
            elif norm(g) < self.t:
                a_max = a

            
            if i > self.MaxInt:
                break
        

        A  = np.sqrt(self.Mu/(4*a)) * np.arctan(alpha/2)
        B  = np.sqrt(self.Mu/(4*a)) * np.arctan(beta/2)
        return a; 


