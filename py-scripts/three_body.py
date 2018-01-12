"""
Extension of the base solution by simulating Venus as a second planet.

Gravitational forces between Mercury and Venus are neglected. 
Only the gravitational force of the Sun on Mercury and Venus is used.
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
rV0 = 10.7   # initial radius of Venus orbit, in units of R0
vV0 = 0.3    # initial orbital speed of Venus, in units of R0/T0
c_a = 1.01   # base acceleration of Mercur, in units of R0/T0**2
rS  = 3.e-7  # Schwarzschild radius of Sun, in units of R0
a2  = 8.2e-7 # specific angular momentum in units of R0**2

# initialize distance and velocity vectors of Mercury and Venus (at perihelion)
vec_rM0 = vector(0, rM0, 0)
vec_vM0 = vector(vM0, 0, 0)
vec_rV0 = vector(0, rV0, 0)
vec_vV0 = vector(vV0, 0, 0)

# define graphical objects; M = Mercury, V = Venus, S = Sun
M = sphere(pos=vec_rM0,         radius=0.5,  color=color.red   )
V = sphere(pos=vec_rV0,         radius=0.5,  color=color.orange)
S = sphere(pos=vector(0, 0, 0), radius=1.5,  color=color.yellow)
# and the initial velocities
M.velocity = vec_vM0
V.velocity = vec_vV0
S.velocity = vector(0, 0, 0)

# add a visible trajectory to Mercury and Venus
M.trajectory = curve(color=color.black, radius=0.005)
V.trajectory = curve(color=color.black, radius=0.005)

def evolve_planet(vec_r_old, vec_v_old, alpha, beta):
    """
    Advance one planet in time by one step of length dt.
    Arguments:
         - vec_r_old: old position vector of planet
         - vec_v_old: old velocity vector of planet
         - alpha: strength of 1/r**3 term in force
         - beta: strength of 1/r**4 term in force
    Returns:
         - vec_r_new: new position vector of planet
         - vec_v_new: new velocity vector of planet
    """

    # compute the factor coming from General Relativity
    fact = 1 + alpha * rS / vec_r_old.mag + beta * a2 / vec_r_old.mag**2
    # compute the absolute value of the acceleration
    a = c_a * fact / vec_r_old.mag**2
    # multiply by the direction to get the acceleration vector
    vec_a = - a * ( vec_r_old / vec_r_old.mag )
    # update velocity vector
    vec_v_new = vec_v_old + vec_a * dt
    # update position vector
    vec_r_new = vec_r_old + vec_v_new * dt
    return vec_r_new, vec_v_new

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
    # update the drawn trajectories with the current position
    M.trajectory.append(pos=M.pos)
    V.trajectory.append(pos=V.pos)
    # update the velocities and positions
    M.pos, M.velocity = evolve_planet(M.pos, M.velocity, alpha, beta)
    V.pos, V.velocity = evolve_planet(V.pos, V.velocity, alpha, beta)
