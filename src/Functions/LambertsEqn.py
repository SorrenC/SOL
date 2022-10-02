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
# Solves lamberts problem given two position measurments, time between said measurments, and the change 
# in true anomaly. 
#
# INPUTS:
#   r1        = position 1 in vector or magnitude
#   r2        = position 2 in vector or magnitude 
#   theta     = change in true anomaly in radians 
#   Mu        = central body orbital parameter 
#   Tolerance = stopping condition for bisection method
#   option    = used to indicate in position given as vector or magnitude 
#
# OUTPUTS:
#   a         = orbit semi major axis
#   c         = chord length between positions 
#   B         =
#   C         =
#
#########################################################################################################

# imports 
import math
import numpy as np
from scipy.linalg import norm 


class LambertsEqn():

    def __init__(self,r1,r2,t,theta,Mu,Tolerance,options):
        self.r1        = r1
        self.r2        = r2
        self.t         = t
        self.theta     = theta
        self.Mu        = Mu
        self.Tolerance = Tolerance
        self.options   = options

    def solve(self):
        
        # Find the chord length between the two positions
        if self.options == 'vector':
            c = np.abs(self.r2 - self.r1) # vector subtraction
        elif self.options == 'magnitude':
            c = np.sqrt(self.r1**2 + self.r2**2 - 2*self.r1*self.r2*np.cos(self.theta)) # law of cosines
        else:
            pass # TO DO: ADD EXCEPTIONS FILE AND CUSTOM EXCEPTIONS

        # Find semi-perimeter 
        s = (c + norm(self.r1) + norm(self.r2))/2;

        # need an initial guess for a and g
        a_min = s/2
        a_max = 2*s
        a     = (a_min + a_max)/2

        # Need an initial guess for alpha, beta, and g 
        alpha = np.arcsin(np.sqrt((s)/(2*a))) * 2
        beta  = np.arcsin(np.sqrt((s-c)/(2*a))) * 2
        g     = np.sqrt((a^3)/(self.Mu)) * (alpha - beta - (np.sin(alpha) - np.sin(beta)))

        # Use bisection method to solve lameberts problem 
        while(np.abs(self.t-g) > self.Tolerance):

            a     = (a_min + a_max)/2
            alpha = np.arcsin(np.sqrt((s)/(2*a))) * 2
            beta  = np.arcsin(np.sqrt((s-c)/(2*a))) * 2
            g     = np.sqrt((a^3)/(self.Mu)) * (alpha - beta - (np.sin(alpha) - np.sin(beta)))

            if g > self.t:
                a_min = a
            elif g < self.t:
                a_max = a
            else:
                break

        return a; 


