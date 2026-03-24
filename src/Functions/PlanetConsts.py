#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    10/1/2022
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## PlanetConsts #################################################
#
# Defines common planetary constants such as gravitational parameter, mass, radius, average density,etc.
# Also includes the J2 pertubations constants, J2 pertubations are due to the oblatness of a planet. See
# conceptual guide document for more information. 
# Data taken from NASA Space Science Data Coordinated Archive (NSSDC)
# WIP: rewrite to use a dataclass+registry, more "pythonic" and easier to scale
#########################################################################################################

# Imports
from dataclasses import dataclass
from typing import Optional

# Create dataclass for storing physical and orbital data of planets and other orbital bodies. Immutable because these values should not change
@dataclass(frozen=True)
class OrbtialBody:
        Name: str                   # 
        mass: float                 # [kg]
        radius_mean: float          # [km]
        radius_equitorial: float    # [km]
        radius_polar: float         # [km]
        mu: float                   # [km^3 / s^2]
        j2: Optional[float]         # [Dimensionless]
        j3: Optional[float]         # [Dimensionless]
        j4: Optional[float]         # [Dimensionless]
        j5: Optional[float]         # [Dimensionless]

SUN = OrbtialBody(
        Name = "Sun",
        mass = 1.988e+30, 
        radius_mean = 6957000, 
        radius_equitorial = None, 
        radius_polar = None, 
        mu = 1.327e+11, 
        j2 = None, 
        j3 = None, 
        j4 = None, 
        j5 = None
)

MERCURY = OrbtialBody(
        Name = "Mercury",
        mass = 0.330e+24, 
        radius_mean = (4879)/2, 
        radius_equitorial = None,
        radius_polar = None,
        mu = 2.2030e+4, 
        j2 = 50.3e-6, 
        j3 = None, 
        j4 = None, 
        j5 = None
)

# Venus
VENUS_MU       = 3.249e+5       # [km^3 / s^2]
VENUS_MASS     = 4.87e+24       # [kg]
VENUS_RADIUS   = (12104)/2      # [km]
VENUS_J2       = 4.458          # [Dimensionless]

# Earth 
EARTH_MU       = 3.986e+5       # [km^3 / s^2]
EARTH_MASS     = 5.97224e+24    # [kg]
EARTH_RADIUS   = 6371           # [km]
EARTH_J2       = 1082.63e-6     # [Dimensionless]

# Mars
MARS_MU        = 4.305e+4       # [km^3 / s^2]   
MARS_MASS      = 0.642e+24      # [kg]
MARS_RADIUS    = (6792)/2       # [km] 
MARS_J2        = 1960.45e-6     # [Dimensionless]

# Jupiter 
JUPITER_MU     = 1.267e+8       # [km^3 / s^2]
JUPITER_MASS   = 1898e+24       # [kg]
JUPITER_RADIUS = (142984)/2     # [km]
JUPITER_J2     = 14736e-6       # [Dimensionless]

# Saturn 
SATURN_MU      = 3.793e+7       # [km^3 / s^2]
SATURN_MASS    = 568e+24        # [kg]
SATURN_RADIUS  = (120536)/2     # [km]
SATURN_J2      = 16298e-6       # [Dimensionless]

# Uranus 
URANUS_MU      = 5.794e+6       # [km^3 / s^2]
URANUS_MASS    = 86.8e+24       # [kg]
URANUS_RADIUS  = (51118)/2      # [km]
URANUS_J2      = 3343.43e-6     # [Dimensionless]

# Neptune 
NEPTUNE_MU     = 6.837e+6       # [km^3 / s^2]
NEPTUNE_MASS   = 102e+24        # [kg]
NEPTUNE_RADIUS = (49528)/2      # [km]
NEPTUNE_J2     = 3411e-6        # [Dimensionless]

