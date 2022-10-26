from mpl_toolkits.mplot3d import Axes3D
import numpy
from matplotlib import pyplot, cm
import time, sys, timeit


### Variable declaration
nx = 81
ny = 81
dx = 2/(nx-1)
dy = 2/(ny-1)
nt = 100
Co = 0.2
dt = dx*Co
c = 1

startTime = timeit.default_timer()  # Define a timer for speed comparison

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((nx,ny))
uN = numpy.ones((nx,ny))

### Assign ICs
u[int(0.5/dx):int(1/dx+1),int(0.5/dy):int(1/dy+1)] = 2

### Plot ICs
fig = pyplot.figure(figsize = (11, 7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
X, Y = numpy.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u[:], cmap = cm.viridis)
# surf2 = ax.plot_surface(X, Y, u[:])
pyplot.show(block = True)

### Calculation with nested for-loops - SLOWER
startTimeFL = timeit.default_timer()

for k in range(nt+1):
    uN = u.copy()
    row, col = u.shape
    for i in range(1, row):
        for j in range(1, col):
            u[i,j] = uN[i,j] - c*dt/dx*(uN[i,j]-uN[i-1,j]) - c*dt/dy*(uN[i,j]-uN[i,j-1])

            u[0, :] = 1             # Value @ bottom horizontal boundary is 1
            u[:, 0] = 1             # Value @ left vertical boundary is 1
            u[-1, :] = 1            # Value @ top horizontal boundary is 1
            u[:, -1] = 1            # Value @ right vertical boundary is 1

fig = pyplot.figure(figsize = (11, 7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap = cm.viridis)
pyplot.show(block = True)

print("For-loop calculation time is:", timeit.default_timer() - startTimeFL,"[s]")

### Calculation with array operations - FASTER
startTimeAO = timeit.default_timer()

u = numpy.ones((nx,ny))
u[int(0.5/dx):int(1/dx+1),int(0.5/dy):int(1/dy+1)] = 2

for k in range(nt+1):
    uN = u.copy()
    u[1:, 1:] = uN[1:, 1:]-c*dt/dx*(uN[1:, 1:]-uN[1:, :-1])-c*dt/dy*(uN[1:, 1:]-uN[:-1, 1:])

    u[0, :] = 1                     # Value @ bottom horizontal boundary is 1
    u[:, 0] = 1                     # Value @ left vertical boundary is 1
    u[-1, :] = 1                    # Value @ top horizontal boundary is 1
    u[:, -1] = 1                    # Value @ right vertical boundary is 1

fig = pyplot.figure(figsize = (11, 7), dpi = 100)
ax = fig.add_subplot(projection = '3d')
surf = ax.plot_surface(X, Y, u[:], cmap = cm.viridis)
pyplot.show(block = True)

print("Array operations calculation time is:", timeit.default_timer() - startTimeAO,"[s]")



