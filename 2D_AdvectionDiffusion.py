from mpl_toolkits.mplot3d import Axes3D

import numpy
from matplotlib import pyplot, cm
import time, sys, timeit


### Declare variables
nx = 41
ny = 41
nt = 120
dx = 2/(nx-1)
dy = 2/(ny-1)
Co = 0.0009
nu = 0.01
dt = Co*dx*dy/nu

### Generate a grid
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((nx, ny))
v = numpy.ones((nx, ny))
uN = numpy.ones((nx, ny))
vN = numpy.ones((nx, ny))

### Assign ICs
u[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2
v[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2

### Plot ICs
fig1 = pyplot.figure(figsize = (11, 7), dpi = 100)
ax1 = fig1.add_subplot(projection = '3d')
X, Y = numpy.meshgrid(x, y)
surf = ax1.plot_surface(X, Y, u[:], cmap = cm.viridis)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('u')
pyplot.show(block = True)
fig2 = pyplot.figure(figsize = (11, 7), dpi = 100)
ax2 = fig2.add_subplot(projection = '3d')
surf2 = ax2.plot_surface(X, Y, v[:], cmap = cm.viridis)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('v')
pyplot.show(block = True)

### Main calculation loop
def Burgers2D(nt,nu):
    for k in range(nt+1):
        uN = u.copy()
        vN = v.copy()
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                u[i,j] = uN[i,j]-uN[i,j]*dt/dx*(uN[i,j]-uN[i-1,j])\
                                -vN[i,j]*dt/dy*(uN[i,j]-uN[i,j-1])\
                                +nu*dt/(dx**2)*(uN[i+1,j]-2*uN[i,j]+uN[i-1,j])\
                                +nu*dt/(dy**2)*(uN[i,j+1]-2*uN[i,j]+uN[i,j-1])

                v[i,j] = vN[i,j]-uN[i,j]*dt/dx*(vN[i,j]-vN[i-1,j])\
                                -vN[i,j]*dt/dy*(vN[i,j]-vN[i,j-1])\
                                +nu*dt/(dx**2)*(vN[i+1,j]-2*vN[i,j]+vN[i-1,j])\
                                +nu*dt/(dy**2)*(vN[i,j+1]-2*vN[i,j]+vN[i,j-1])

                u[0,:] = 1
                v[0,:] = 1
                u[:,0] = 1
                v[:,0] = 1
                u[-1,:] = 1
                v[-1,:] = 1
                u[:,-1] = 1
                v[:,-1] = 1


### Plot results 
    fig3 = pyplot.figure(figsize = (11,7), dpi = 100)
    ax3 = fig3.add_subplot(projection = '3d')
    surf3 = ax3.plot_surface(X, Y, u, cmap = cm.viridis, rstride = 1, cstride = 1)
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_zlabel('u')
    pyplot.show(block = True)
    fig4 = pyplot.figure(figsize = (11,7), dpi = 100)
    ax4 = fig4.add_subplot(projection = '3d')
    surf4 = ax4.plot_surface(X, Y, v, cmap = cm.viridis, rstride = 1, cstride = 1)
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('v')
    pyplot.show(block = True)

            


