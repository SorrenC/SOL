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

VENUS = OrbtialBody(
        Name = "Venus",
        mass = 4.87e+24, 
        radius_mean = (12104)/2, 
        radius_equitorial = None,
        radius_polar = None,
        mu = 3.249e+5, 
        j2 = 4.458, 
        j3 = None, 
        j4 = None, 
        j5 = None
)

EARTH = OrbtialBody(
        Name = "Earth",
        mass = 5.97224e+24,
        radius_mean = 6371,
        radius_equitorial = 6378.137,
        radius_polar = 6356.752,
        mu = 3.986e+5,
        j2 = 1082.63e-6,
        j3 = None,
        j4 = None,
        j5 = None
)

MARS = OrbtialBody(
        Name = "Mars",
        mass = 0.642e+24,
        radius_mean = (6792)/2,
        radius_equitorial = None,
        radius_polar = None,
        mu = 4.305e+4,
        j2 = 1960.45e-6,
        j3 = None,
        j4 = None,
        j5 = None
)

JUPITER = OrbtialBody(
        Name = "Jupiter",
        mass = 1898e+24,
        radius_mean = (142984)/2,
        radius_equitorial = None,
        radius_polar = None,
        mu = 1.267e+8,
        j2 = 14736e-6,
        j3 = None,
        j4 = None,
        j5 = None
)
 
SATURN = OrbtialBody(
        Name = "Saturn",
        mass = 568e+24,
        radius_mean = (120536)/2,
        radius_equitorial = None,
        radius_polar = None,
        mu = 3.793e+7,
        j2 = 16298e-6,
        j3 = None,
        j4 = None,
        j5 = None
 )

URANUS = OrbtialBody(
        Name = "Uranus",
        mass = 86.8e+24,
        radius_mean = (51118)/2,
        radius_equitorial = None,
        radius_polar = None,
        mu = 5.794e+6,
        j2 = 3343.43e-6,
        j3 = None,
        j4 = None,
        j5 = None
)

NEPTURE = OrbtialBody(
        Name = "Neptune",
        mass = 102e+24,
        radius_mean = (49528)/2,
        radius_equitorial = None,
        radius_polar = None,
        mu = 6.837e+6,
        j2 = 3411e-6,
        j3 = None,
        j4 = None,
        j5 = None
)