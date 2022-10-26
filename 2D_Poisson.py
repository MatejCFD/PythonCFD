from mpl_toolkits.mplot3d import Axes3D

import numpy
from matplotlib import pyplot, cm
import timeit, sys, time


### Declare variables
nx = 50
ny = 50
xMin = 0
xMax = 2
yMin = 0
yMax = 1
nt = 100                            # Pseudo-time

dx = (xMax - xMin)/(nx - 1)
dy = (yMax - yMin)/(ny - 1)

### Create a numeric grid
x = numpy.linspace(xMin, xMax, nx)
y = numpy.linspace(yMin, yMax, ny)

### Assign ICs
p = numpy.zeros((nx, ny))
b = numpy.zeros((nx, ny))


### Assign BCs
p[:,0] = 0                          #   Dirichlet BCs    #
p[:,2] = 0                          #                    #
p[0,:] = 0                          #                    # 
p[1,:] = 0                          # for the variable p #

b[int(nx/4),int(ny/4)] = 100        #   Dirichlet BCs    #
b[int(3*nx/4),int(3*ny/4)] = -100   #   for the source   #

### Main calculation
startTime = timeit.default_timer()
for n in range(nt):
    pN = p.copy()

    p[1:-1,1:-1] = ((pN[1:-1,2:]+pN[1:-1,0:-2])*(dy**2)+(pN[2:,1:-1]+pN[0:-2,1:-1])*(dx**2)\
                    -(b[1:-1,1:-1]*(dy**2*dx**2)))/(2*(dx**2+dy**2))

    p[0,:] = 0
    p[ny-1,:] = 0
    p[:,0] = 0
    p[:,nx-1] = 0

print("Calculation done...\nCalculation time:",timeit.default_timer() - startTime,"[s].")

def plot2D(x, y, p):
    fig = pyplot.figure(figsize = (11, 7), dpi = 100)
    ax = fig.add_subplot(projection = '3d')
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, p, cmap = cm.viridis, cstride = 1, rstride = 1, linewidth = 0,antialiased = False)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('p')
    ax.view_init(30, 225)
    pyplot.show(block = True)




