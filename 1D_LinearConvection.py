# Comments in python are denoted by the ampersand symbol

import numpy                        # here we load numpy
from matplotlib import pyplot       # here we load matplotlib
import time, sys                    # and load some utilities

nx = 41                             # Change the number of points
dx = 2/(nx-1)                       # [m]  One grid point
nt = 25                             # Number of timesteps to calculate
dt = 0.025                          # [s] Amout of time each timestep covers
#c = 1
c = numpy.linspace(0,1,11)          # [m/s] Wavespeed
L = len(c)

u = numpy.ones(nx)                  # Assign a velocity value to the each gridpoint
#u[int(0.5/dx):int(1/dx+1)] = 2     # Set up the IC given: u = 2, for x in [0.5,1]
#print(u)


# pyplot.plot(numpy.linspace(0,2,nx),u);
# pyplot.show(block=True)           # run with python -i script.py (exit with Ctrl+D)
for j in range(L):
    u[int(0.5/dx):int(1/dx+1)] = c[j]

    un = numpy.ones(nx)             # Initialize a temporary holder array

    for i in range(nt):             # First loop: for i < all the timesteps
        un = u.copy()               # Take existing values of u (with the IC specified...)
        # for i in range(1, nx):
        for i in range(nx):         # Compare with the previous line
            u[i] = un[i] - c[j]*(dt/dx)*(un[i] - un[i-1])

    print(u)
    flag = "c=%s" % str(round(c[j],2))
    fflag = "c % s" % str(round(c[j],2))
    pyplot.plot(numpy.linspace(0,2,nx),u)
    ax = pyplot.gca()
    ax.set_ylim(0,1.2)
    pyplot.title("%s" % flag)
    pyplot.savefig("%s.png" % fflag)
    pyplot.show(block=True)

