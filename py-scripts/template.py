"""
A template for the simulation of Mercuries orbit.

Sets up the graphics display and defines basic parameters like the position and
velocity of Mercury. Also provides a basic structure for the program to get started
quickly.

All parts that have to be filled in are marked by '### TODO' and brief descriptions
of the tasks.

Run parameters are given just before the while loop at the end. They can be
changed freely but the values given have proven to yield good results.
"""

# Import everything from vpython (need graphics output, vectors, etc.)
from vpython import *

# Set up display
scene.width      = 1680
scene.height     = 1024
scene.background = color.white
scene.center     = vector(0, -2, 0)

# Definition of parameters
# Values computed using https://nssdc.gsfc.nasa.gov/planetary/factsheet
rM0 = 4.60    # Initial radius of Mercury orbit, in units of R0
vM0 = 5.10e-1 # Initial orbital speed of Mercury, in units of R0/T0
c_a = 9.90e-1 # Base acceleration of Mercury, in units of R0**3/T0**2
rS  = 2.95e-7 # Schwarzschild radius of Sun,in units of R0
rL2 = 8.19e-7 # Specific angular momentum, in units of R0**2


# Initialize distance and velocity vectors of Mercury (at perihelion)
vec_rM0 = vector(0, rM0, 0)
vec_vM0 = vector(vM0, 0, 0)


# Define graphical objects; M = Mercury, S = Sun ...
S = sphere(pos=vector(0, 0, 0), radius=1.5,  color=color.yellow)
### TODO
#  - Define graphical Mercury objects that you want to display.
#  - Give Mercury initial positions and velocities.
#  - Enable drawing of trajectory of Mercury by using the 'curve' object


def evolve_mercury(vec_rM_old, vec_vM_old, alpha, beta):
    """
    Advance Mercury in time by one step of length dt.
    Arguments:
         - vec_rM_old: old position vector of Mercury
         - vec_vM_old: old velocity vector of Mercury
         - alpha: strength of 1/r**3 term in force
         - beta: strength of 1/r**4 term in force
    Returns:
         - vec_rM_new: new position vector of Mercury
         - vec_vM_new: new velocity vector of Mercury
    """

    ### TODO
    #  - Calculate new position and velocity of Mercury here.
    # vec_rM_new = ??
    # vec_vM_new = ??

    return vec_rM_new, vec_vM_new

# Define run parameters
dt = 2. * vM0 / c_a / 20  # Time step
alpha = 1.e6              # Strength of 1/r**3 term
beta = 0.0                # Strength of 1/r**4 term
time = 0                  # Current simulation time
max_time = 1000*dt        # Maximum simulation time

# Run the simulation for a given time and draw trajectory
while time < max_time:
    # Set the frame rate: shows four earth days at once
    rate(100)

    ### TODO
    #  - Append the mercury position to it's trajectory.
    #  - Update position and velocity of Mercury (see function evolve_mercury).
