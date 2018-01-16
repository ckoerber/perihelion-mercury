"""
Extension of the base solution to measure and display the preihelion.

Extends 'base_solution.py' by keeping track of the location of the perihelion
of Mercury. Computes and outputs the angle by which the perihelion changes over
the course of the simulation.

The stopping criterion is different than in 'base_solution.py'. 
This code uses a fixed number of revolutions around the sun instead of a 
fixed run time.
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
ra2 = 8.19e-7 # Specific angular momentum, in units of R0**2


# Initialize distance and velocity vectors of Mercury (at perihelion)
vec_rM0 = vector(0, rM0, 0)
vec_vM0 = vector(vM0, 0, 0)

# Define graphical objects; M = Mercury, S = Sun ...
M = sphere(pos=vec_rM0,         radius=0.5,  color=color.red   )
S = sphere(pos=vector(0, 0, 0), radius=1.5,  color=color.yellow)
# ... and the initial velocities
M.velocity = vec_vM0
S.velocity = vector(0, 0, 0)

# Add a visible trajectory to Mercury
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

    # Compute the factor coming from General Relativity
    fact = 1 + alpha * rS / vec_rM_old.mag + beta * ra2 / vec_rM_old.mag**2
    # Compute the absolute value of the acceleration
    aMS = c_a * fact / vec_rM_old.mag**2
    # Multiply by the direction to get the acceleration vector
    vec_aMS = - aMS * ( vec_rM_old / vec_rM_old.mag )
    # Update velocity vector
    vec_vM_new = vec_vM_old + vec_aMS * dt
    # Update position vector
    vec_rM_new = vec_rM_old + vec_vM_new * dt
    return vec_rM_new, vec_vM_new

# Provide function to compute angle between vectors
def angle_between(v1, v2):
    """Compute angle between two vectors. Result is in degrees."""
    return acos( dot(v1, v2) / (v1.mag * v2.mag) ) * 180. / pi

# Define run parameters and help variables
dt = 2. * vM0 / c_a / 200 # Time step
alpha      = 0.0          # Strength of 1/r**3 term
beta       = 1.e5         # Strength of 1/r**4 term
vec_r_last = vec_rM0      # Previous position of Mercury
turns      = 0            # Number of completed turns
max_turns  = 10           # Maximum number of turns
list_perih = list()       # List of perihelion locations
sum_angle  = 0.           # Angle between first and last perihelion

# Find perihelion for each turn and print it out
while turns < max_turns:
    vec_r_before_last = vec_r_last
    vec_r_last        = vector(M.pos)
    # Set the frame rate: shows four earth days at once
    rate(100)
    # Update the drawn trajectory with the current position
    M.trajectory.append(pos=M.pos)
    # Update the velocity and position
    M.pos, M.velocity = evolve_mercury(M.pos, M.velocity, alpha, beta)
    # Check if just past perihelion
    if vec_r_before_last.mag > vec_r_last.mag < M.pos.mag:
        turns = turns+1
        list_perih.append(vec_r_last)
        if turns > 1:
            # Draw location of perihelion
            sphere(color=color.green, radius=0.2, pos=vec_r_last)
            # Display intermediate results
            print("turn: n={n}, perihelion growth: delta Theta={angle}".format(
                n=turns, angle=angle_between(list_perih[-2], list_perih[-1])
            ))
            # Note that list_perih[-2] accesses the second last and
            #  list_perih[-1] the last element in the list
            sum_angle = sum_angle + angle_between(list_perih[-2], list_perih[-1])

# Display the average perihelion growth
print("--------------------------------")
print("Average perihelion growth in arc sec per century: delta Theta={avg:1.2f}".format(
    avg=sum_angle/(len(list_perih)-1) * 3. / beta * 3600 * 4.15 * 100 
))
