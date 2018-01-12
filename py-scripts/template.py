"""
Template for the simulation of Mercuries orbit.

Sets up the graphics display and defines basic parameters like the position and
velocity of Mercury. Also provides a basic structure for the program to get started
quickly.

All parts that have to be filled in are marked by '### TODO' and brief descriptions
of the tasks.

Run parameters are given just before the while loop at the end. They can be
changed freely but the values given have proven to yield good results.
"""

# import everything from vpython (need graphics output, vectors, etc.)
from vpython import *

# set up display
scene.width      = 1680
scene.height     = 1024
scene.background = color.white
scene.center     = vector(0, -2, 0)

# definition of parameters
# values computed using https://nssdc.gsfc.nasa.gov/planetary/factsheet
rM0 = 4.6    # initial radius of Mercury orbit, in units of R0
vM0 = 0.51   # initial orbital speed of Mercury, in units of R0/T0
c_a = 1.01   # base acceleration of Mercur, in units of R0/T0**2
rS  = 3.e-7  # Schwarzschild radius of Sun, in units of R0
a2  = 8.2e-7 # specific angular momentum in units of R0**2

# initialize distance and velocity vectors of Mercury (at perihelion)
vec_rM0 = vector(0, rM0, 0)
vec_vM0 = vector(vM0, 0, 0)

### TODO
#  - Define graphical objects that you want to display.
#  - Give them initial positions and velocities.
#  - Enable drawing of trajectory of Mercury.

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

# run parameters
dt = 2. * vM0 / c_a / 20  # time step
alpha   = 1.e6            # strength of 1/r**3 term
beta = 0.0                # strength of 1/r**4 term
time = 0                  # current simulation time
max_time = 1000*dt        # maximum simulation time

# run the simulation for a given time and draw trajectory
while time < max_time:
    # set the frame rate: shows four earth days at once
    rate(100)

    ### TODO
    #  - Append position to trajectory.
    #  - Update position and velocity of Mercury (see function evolve_mercury).
