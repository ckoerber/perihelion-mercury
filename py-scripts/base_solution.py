"""
Solution to the base problem.

Simulates the movement of Mercury and displays its position and a trajectory at
regular intervals.
The additional term ~ alpha/r**3 and ~ beta/r**4 are included in the force.
In order to simulate without it, simply set alpha=0=beta before the while loop.
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

# define graphical objects; M = Mercury, S = Sun
M = sphere(pos=vec_rM0,         radius=0.5,  color=color.red   )
S = sphere(pos=vector(0, 0, 0), radius=1.5,  color=color.yellow)
# and the initial velocities
M.velocity = vec_vM0
S.velocity = vector(0, 0, 0)

# add a visible trajectory to Mercury
M.trajectory = curve(color=color.black, radius=0.005)

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

    # compute the factor coming from General Relativity
    fact = 1 + alpha * rS / vec_rM_old.mag + beta * a2 / vec_rM_old.mag**2
    # compute the absolute value of the acceleration
    aMS = c_a * fact / vec_rM_old.mag**2
    # multiply by the direction to get the acceleration vector
    vec_aMS = - aMS * ( vec_rM_old / vec_rM_old.mag )
    # update velocity vector
    vec_vM_new = vec_vM_old + vec_aMS * dt
    # update position vector
    vec_rM_new = vec_rM_old + vec_vM_new * dt
    return vec_rM_new, vec_vM_new

# run parameters
dt = 2. * vM0 / c_a / 20  # time step
alpha = 1.e6              # strength of 1/r**3 term
beta = 0.0                # strength of 1/r**4 term
time = 0                  # current simulation time
max_time = 1000*dt        # maximum simulation time

# run the simulation for a given time and draw trajectory
while time < max_time:
    # set the frame rate: shows four earth days at once
    rate(100)
    # update the drawn trajectory with the current position
    M.trajectory.append(pos=M.pos)
    # update the velocity and position
    M.pos, M.velocity = evolve_mercury(M.pos, M.velocity, alpha, beta)