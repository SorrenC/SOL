#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    09/29/2022
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## Utilities ####################################################
#
# Collection of classes and functions used by most other functions. i.e functions to check user data and
# stuff of that nature. Also contains common math and astrodynamics functions not large enough to 
# warrant their own class/file
#
#########################################################################################################

# imports 
import numpy as np
import numpy.typing as npt
import math  as m

######################################## Mathematic Functions ###########################################
#
# Simple mathematic functions that do not warrant their own class/function file. 
#
#########################################################################################################

# Input angle in RADIANS and return the cotangent of that angle 
def cotan(theta):
    return (1)/(np.tan(theta))

# Input graviational parameter and circular orbit radius and return constant velocity of circular orbit
def CircularVelocity(Mu,r):
    return np.sqrt(Mu/r)

# Input graviational parameter, semi-major axis, and orbital eccentricity and return the velocity 
# at periapse of the described orbit
def PeriapseVelocity(Mu,a,e):
    return np.sqrt((Mu/a)*((1+e)/(1-e)))

# Input graviational parameter, semi-major axis, and orbital eccentricity and return the velocity 
# at apoapse of the described orbit
def ApoapseVelocity(Mu,a,e):
    return np.sqrt((Mu/a)*((1-e)/(1+e)))

# Input gravitational parameter, semi-major axis, and position vector at some point along the objects
# orbit and return the velocity of the object at that specific point in the orbit
def VisViva(Mu,a,r):
    return np.sqrt(Mu*((2/r)-(1/a)))


######################################## Type Aliases ###################################################
#
# Create type aliases for numpy datatypes such as ndarray and float64, makes it easier to read
#
#########################################################################################################

FloatArray64 = npt.NDArray[np.float64]      # Type alias for numpy array of 64 bit floats
Array = npt.NDArray                         # Type alias for numpy array of any type    
Float64 = np.float64                        # Type alias for 64 bit float  