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
# measurments. The program assumes an elliptical orbit. Returns a list
# This solver uses a bisection algorithm to solve Lamberts equation for semi-major axis
#
# INPUTS:
#   r1        = position 1 in vector or magnitude. Either python list or numpy array 
#   r2        = position 2 in vector or magnitude. Either python list or numpy array
#   t         = time between position vectors
#   Mu        = central body orbital parameter 
#   Tolerance = stopping condition for numerical method
#   MaxInt    = maximum iterations before algorithm stops 
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

    def BiSection(self):
        
        # check if supplied vectors are a list or a numpy array, convert to numpy array if not
        if isinstance(self.r1, np.ndarray)   == True:
            pass
        elif isinstance(self.r1, np.ndarray) == False:
            self.r1 = np.asarray(self.r1)
        else:
            raise BAD_INPUT
        
        if isinstance(self.r2, np.ndarray)   == True:
            pass
        elif isinstance(self.r2, np.ndarray) == False:
            self.r2 = np.asarray(self.r2)
        else:
            raise BAD_INPUT

        # Find the chord length between the two positions
        if self.options == 'vector':
            c     = norm(self.r2 - self.r1) # vector subtraction
        elif self.options == 'magnitude':
            theta = np.arccos((np.dot(self.r1,self.r2))/(norm(self.r1) * norm(self.r2))) # angle between two vectors
            c     = np.sqrt(self.r1**2 + self.r2**2 - 2*self.r1*self.r2*np.cos(theta))   # law of cosines
        else:
            raise BAD_INPUT
        
        # Find semi-perimeter 
        s = (c + norm(self.r1) + norm(self.r2))/2;

        # need an initial guess for a and delta T
        a_min = s/2
        a_max = 2*s
        a     = (a_min + a_max)/2
        alpha = (np.arcsin(np.sqrt((s)/(2*a))))   * 2
        beta  = (np.arcsin(np.sqrt((s-c)/(2*a)))) * 2
        g     = np.sqrt((a**3)/(self.Mu)) * (alpha - beta - (np.sin(alpha) - np.sin(beta)))

        # create iteration counter
        i = 1

        # Use bisection method to solve lameberts problem for semi major axis
        while(np.abs(self.t-norm(g)) > self.Tolerance):
            i     = i+1
            a     = (a_min + a_max)/2
            alpha = (np.arcsin(np.sqrt((s)/(2*a)))) * 2
            beta  = (np.arcsin(np.sqrt((s-c)/(2*a)))) * 2
            g     = np.sqrt((a**3)/(self.Mu)) * (alpha - beta - (np.sin(alpha) - np.sin(beta)))
 
            # bisection method
            if norm(g) > self.t:
                a_min = a
            elif norm(g) < self.t:
                a_max = a
 
            if i > self.MaxInt:
                raise MAX_ITERATIONS_REACHED
        
        # Find velocity at positions one and position two 
        A  = (np.sqrt(self.Mu/(4*a))) * (np.arctan(alpha/2))
        B  = (np.sqrt(self.Mu/(4*a))) * (np.arctan(beta/2))

        u1 = (self.r1) / (norm(self.r1))
        u2 = (self.r2) / (norm(self.r2))
        uc = (self.r2 - self.r1)/c

        v1 = ((B+A)*uc) + ((B-A)*u1)
        v2 = ((B+A)*uc) - ((B-A)*u2)

        # return a list of vectors/magnitudes
        return a,v1,v2


# THIS IS ONLY FOR TESTING, DELETE LATER AND MOVE TO SEPARATE TEST FILE 
if __name__ == '__main__':
    # This example is the position of Mars from the sun body center taken 1 full day apart
    r1_vector = [1.705762706464142E+08,1.331457466962230E+08,-1.393668994909272E+06]  # [km]
    r2_vector = [1.693596693212054E+08,1.349683079588937E+08,-1.325628359792881E+06]  # [km]
    t         = 24*60*60                                                              # [s]
    Mu        = 1.327e+11                                                             # [km^3/s^2]
    Tolerance = 0.0001
    MaxInt    = 5000


    vec_solution=LambertsSolver(r1_vector,r2_vector,t,Mu,Tolerance,MaxInt,'vector')
    solution= vec_solution.BiSection()

    # Function returns a tuple of numpy arrays, extract data from 'solution'
    print(solution[0])
    print(solution[1])
    print(solution[2])