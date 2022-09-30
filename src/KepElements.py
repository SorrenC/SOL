#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    09/29/2022
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## KepElements ##################################################
#
# Class to solve for the six Keplerian orbital elements given state vectors postion and velocity as well
# as the graviational parmater of the central body
# NOTE: The returned vectors have not been normalized, use the function
# numpy.norm() to do so. Futhurmore all applicable value are returned in degrees. 
# Equations taken from Prussing and Conway
#
#########################################################################################################

### Imports ###
import math  as m 
import numpy as np
from scipy.linalg import norm 


### Class Definition ###
class KepElements():

    # Class variables
    def __init__(self,r,v,Mu):
        self.r  = r                             # Postion state vector
        self.v  = v                             # Velocity state vector 
        self.Mu = Mu                            # Gravitation parameter of central body
        self.h  = np.cross(self.r,self.v)       # find momentum vector
        self.n  = np.cross([0,0,1],self.h)      # find line of nodes vector

    # Eccentricity 
    def Eccentricity(self):
        e = ((1.0/self.Mu) * np.cross(self.v,self.h)) - (np.array(self.r)/norm(self.r))     # find eccentricity vector
        return e

    # Orbital inclination
    def inclination(self):
        i = (np.arccos(np.dot((self.h/norm(self.h)),np.array([0,0,1])))) * (180/m.pi)     # find orbital inclination, and convert to degrees
        return i 

    # Semi major axis
    def SemiMjAxis(self):
        E = (((norm(v))**2)/2) - (self.Mu/norm(r))       # Find total energy of orbit 
        a = -(self.Mu/(2*E))                        # Find semi major axis of orbit
        return a

    # Right Ascension of Ascending Node
    def RAAN(self):
        W = (np.arccos(np.dot([1,0,0],(self.n/norm(self.n))))) * (180/m.pi)     # Find Right Ascension of Ascending Note, and convert to degrees

        # Need to check for quadrant ambiguity 
        if np.dot([0,1,0],self.n) < 0:
            W = 360 - W
        else:
            pass # do nothing, in the correct quadrant
        return W

    # Argument of Perigee
    def AOP(self):
        e = ((1.0/self.Mu) * np.cross(self.v,self.h)) - (np.array(self.r)/norm(self.r))   # find eccentricity vector
        w = np.arccos((np.dot(self.n,e)) / (norm(self.n) * norm(e))) * (180/np.pi)        # Find Argument of Perigee (and convert to degrees)

        # Need to check for quadrant ambiguity 
        if np.dot([0,0,1],e) < 0:
            w = 360 - w;
        else: 
            pass # do nothing, in the correct quadrant 
        return w

    # True Anomaly
    def TrueAnmly(self):
        e = ((1.0/self.Mu) * np.cross(self.v,self.h)) - (np.array(self.r)/norm(self.r))   # find eccentricity vector
        f = np.arccos((np.dot(self.r,e)) / (norm(self.r)*norm(e))) * (180/np.pi)          # Find True anamoly (and convert to degrees)

        #Need to check for quadrant ambiguity
        if np.dot(r,v) < 0:
            f = 360 - f;
        else:
            pass  # do nothing, in the right quadrant 
        return f



# Test to ensure that functions are accurate and working corrctly

# State vectors from sun to Mars
r  = [1.692167431596910e+08,1.332858910440899e+08,-1.363164898702294e+06]
v  = [-1.398517076752354e+01, 2.115435793447175e+01, 7.868656661555926e-01]
Mu = 132700000000

d     = KepElements(r,v,Mu)
eccen = d.Eccentricity()
inc   = d.inclination()
a     = d.SemiMjAxis()
Raan  = d.RAAN()
Aop   = d.AOP()
TrAnm = d.TrueAnmly()

print("Eccentricity:        %.3f" % norm(eccen))
print("Orbital Inclination: %.3f deg" %inc)
print("SemiMajor Axis:      %.3f km" %norm(a))
print("R.A.A.N:             %.3f" %Raan)
print("Argument of Perigee  %.3f" %Aop)
print("True Anomaly:        %.3f deg" %TrAnm)
