from mpl_toolkits.mplot3d import Axes3D 

import numpy
from matplotlib import pyplot, cm
import time, sys, timeit


### Declare variables
nx = 31
ny = 31
nt = 17
dx = 2/(nx-1)
dy = 2/(ny-1)
Co = 0.25
nu = 0.05
dt = Co*dx*dy/nu

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((nx, ny))
uN = numpy.ones((nx, ny))

### Assign ICs

u[int(0.5/dx):int(1/dx+1), int(0.5/dx):int(1/dy+1)] = 2

### Plot ICs
fig = pyplot.figure(figsize = (11,7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
X, Y = numpy.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u, cmap = cm.viridis)
ax.set_xlabel('x')
ax.set_ylabel('y')
pyplot.show(block = True)

### For-loop calculation
startTimeFL = timeit.default_timer()

for k in range(nt+1):
    uN = u.copy()
    
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u[i,j] = uN[i,j]+nu*dt/(dx**2)*(uN[i+1,j]-2*uN[i,j]+uN[i-1,j])\
                            +nu*dt/(dy**2)*(uN[i,j+1]-2*uN[i,j]+uN[i,j-1])

            u[0,:] = 1
            u[:,0] = 1
            u[-1,:] = 1
            u[:,-1] = 1

fig = pyplot.figure(figsize = (11, 7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
surf = ax.plot_surface(X, Y, u, cmap = cm.viridis)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_zlim(1, 2.5)
pyplot.savefig("FL.png")
pyplot.show(block = True)

print("For-loop took:", timeit.default_timer() - startTimeFL,"[s]")
print(u)

### Array operations

def Diffusion2D(nt):
    startTimeAO = timeit.default_timer()

    u = numpy.ones((nx, ny))
    u[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2

    for n in range(nt+1):
        uN = u.copy()
        u[1:-1,1:-1] = uN[1:-1,1:-1]+nu*dt/(dx**2)*(uN[1:-1,2:]-2*uN[1:-1,1:-1]+uN[1:-1,0:-2])\
                                    +nu*dt/(dy**2)*(uN[2:,1:-1]-2*uN[1:-1,1:-1]+uN[0:-2,1:-1])

        u[0,:] = 1
        u[:,0] = 1
        u[-1,:] = 1
        u[:,-1] = 1

    fig = pyplot.figure(figsize = (11, 7), dpi = 100)
    ax = fig.add_subplot(projection = '3d')
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, u, cmap = cm.viridis)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_zlim(1, 2.5)
    pyplot.savefig("AO.png")
    pyplot.show(block = True)

    print("Array operations took:", timeit.default_timer() - startTimeAO,"[s]")
    print(u)


