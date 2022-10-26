from mpl_toolkits.mplot3d import Axes3D

import numpy
from matplotlib import pyplot, cm
import time, sys, timeit



### Variable declaration
nx = 101
ny = 101
nt = 100
dx = 2/(nx-1)
dy = 2/(ny-1)
Co = 0.2
dt = dx*Co

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((nx, ny))
v = numpy.ones((nx, ny))
uN = numpy.ones((nx, ny))
vN = numpy.ones((nx, ny))

### Assign ICs

u[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2
v[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2

fig = pyplot.figure(figsize = (11, 7), dpi = 100)
X, Y = numpy.meshgrid(x, y)
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, u, cmap = cm.viridis, rstride = 2, cstride = 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
pyplot.show(block = True)

### Calculation with the help of nested for-loops
startTimeFL = timeit.default_timer()

for k in range(nt+1):
    uN = u.copy()
    vN = v.copy()
    row_u, col_u = u.shape
    row_v, col_v = v.shape
    for i in range(1, row_u):
        for j in range(1, col_u):
            u[i,j] = uN[i,j]-uN[i,j]*dt/dx*(uN[i,j]-uN[i-1,j])-vN[i,j]*dt/dy*(uN[i,j]-uN[i,j-1])
            
            u[0, :] = 1
            u[:, 0] = 1
            u[-1, :] = 1
            u[:, -1] = 1
            v[i,j] = vN[i,j]-uN[i,j]*dt/dx*(vN[i,j]-vN[i-1,j])-vN[i,j]*dt/dy*(vN[i,j]-vN[i,j-1])
            
            v[0, :] = 1
            v[:, 0] = 1
            v[-1, :] = 1
            v[:, -1] = 1

fig = pyplot.figure(figsize = (11,7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, u, cmap = cm.viridis, rstride = 2, cstride = 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
pyplot.show(block = True)

fig = pyplot.figure(figsize = (11,7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, v, cmap = cm.viridis, rstride = 2, cstride = 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
pyplot.show(block = True)

print("For-loops took:",timeit.default_timer() - startTimeFL,"[s]")

### Calculation with the help of array operations
startTimeAO = timeit.default_timer()

u = numpy.ones((nx, ny))
v = numpy.ones((nx, ny))
uN = numpy.ones((nx, ny))
vN = numpy.ones((nx, ny))

u[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2
v[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2

for l in range(nt+1):
    uN = u.copy()
    vN = v.copy()

    u[1:,1:] = uN[1:,1:]-uN[1:,1:]*dt/dx*(uN[1:,1:]-uN[1:,:-1]) \
                        -vN[1:,1:]*dt/dy*(uN[1:,1:]-uN[:-1,1:])

    v[1:,1:] = vN[1:,1:]-uN[1:,1:]*dt/dx*(vN[1:,1:]-vN[1:,:-1]) \
                        -vN[1:,1:]*dt/dy*(vN[1:,1:]-vN[:-1,1:])

    u[0, :] = 1
    u[:, 0] = 1
    u[-1, :] = 1
    u[:, -1] = 1

    v[0, :] = 1
    v[:, 0] = 1
    v[-1, :] = 1
    v[:, -1] = 1

fig = pyplot.figure(figsize = (11,7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, u, cmap = cm.viridis, rstride = 2, cstride = 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
pyplot.show(block = True)

fig = pyplot.figure(figsize = (11, 7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, v, cmap = cm.viridis, rstride = 2, cstride = 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
pyplot.show(block = True)


print("Array operations took:",timeit.default_timer() - startTimeAO,"[s]")

