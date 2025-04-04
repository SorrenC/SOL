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
from Exceptions import BAD_INPUT


### Class Definition ###
class KepElements():

    # Class variables
    def __init__(self,r,v,Mu):
        self.r  = r                             # Postion state vector
        self.v  = v                             # Velocity state vector 
        self.Mu = Mu                            # Gravitation parameter of central body

        # Check if supplied position vector is a numpy array; if list is supplied then convert it to a numpy array
        if isinstance(self.r , np.ndarray) == True:
            pass 
        elif (isinstance(self.r, list)) == True:
            self.r = np.asarray(self.r) 
        elif (isinstance(self.r,np.ndarray)) or (isinstance(self.r,list)) == False:
            raise BAD_INPUT

        # Check if supplied velocity vector is a numpy array; if list is supplied then convert it to a numpy array
        if isinstance(self.v , np.ndarray) == True:
            pass 
        elif (isinstance(self.v, list)) == True:
            self.v = np.asarray(self.v) 
        elif (isinstance(self.v,np.ndarray)) or (isinstance(self.v,list)) == False:
            raise BAD_INPUT

        # Values pertinent to all classical orbital elements
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
    def SemiMajorAxis(self):
        E = (((norm(self.v))**2)/2) - (self.Mu/norm(self.r))       # Find total energy of orbit 
        a = -(self.Mu/(2*E))                                       # Find semi major axis of orbit
        return a

    # Longitude of Ascending Node a.k.a Right Ascension of Ascending Node
    def RAAN(self):
        #N_vector = np.cross([0,0,1],self.h)
        #W = (np.arccos((N_vector[0])/(norm(N_vector)))) * (180/m.pi)           # Find Right Ascension of Ascending Note, and convert to degrees
        W = (np.arccos(np.dot([1,0,0],(self.n/norm(self.n))))) * (180/m.pi)     # Find Right Ascension of Ascending Note, and convert to degrees

        # Need to check for quadrant ambiguity 
        if np.dot([0,1,0],self.n) < 0:
            W = 360 - W
        else:
            pass # do nothing, in the correct quadrant
        return W

    # Argument of Periapsis
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
    def TrueAnomaly(self):
        e = ((1.0/self.Mu) * np.cross(self.v,self.h)) - (np.array(self.r)/norm(self.r))   # find eccentricity vector
        f = np.arccos((np.dot(self.r,e)) / (norm(self.r)*norm(e))) * (180/np.pi)          # Find True anamoly (and convert to degrees)

        #Need to check for quadrant ambiguity
        if np.dot(self.r,self.v) < 0:
            f = 360 - f;
        else:
            pass  # do nothing, in the right quadrant 
        return f
    
    # Solve all orbital elements; return results in a numpy array
    def SolveAll(self):
        e = self.Eccentricity()
        i = self.inclination()
        a = self.SemiMajorAxis()
        W = self.RAAN()
        w = self.AOP()
        f = self.TrueAnomaly()

        return np.array([e,i,a,W,w,f],dtype=object)
    
    def RaanJ2(self,J2,R,a,e,i):
        #
        # RaanJ2
        # 
        # Calculates the effect of J2 pertubations on the RAAN as a function of time i.e d(Omega)/dt
        #
        # Inputs:
        #       J2 = J2 constant                                    [dimensionless]
        #       R  = Radius of central body                         [km]
        #       a  = semi-major axis of the orbiting bodies orbit   [km]
        #       e  = eccentricity of the orbiting bodies orbit      [dimensionless]
        #       i  = orbital inclination of orbiting body           [rad]
        #
        # Outputs:
        #       dWdt
        
        # Curtis pg. 197 1st ed eqn. 4.47
        dWdt = -((3/2)*(((np.sqrt(self.Mu))*(J2)*(R**2))/(  ((1-e**2)**2)*(a**(7/2)))))*(np.cos(i))

        return dWdt

