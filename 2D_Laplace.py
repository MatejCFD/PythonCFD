from mpl_toolkits.mplot3d import Axes3D

import numpy
from matplotlib import pyplot, cm
import timeit, sys, time


### Declare variables
nx = 81
ny = 81
nt = 100
dx = 2/(nx-1)
dy = 2/(ny-1)


### Define the grid
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 1, ny)


### Assign ICs
p = numpy.zeros((nx, ny))

### Assign BCs
p[:,0] = 0                                      # Dirichlet BC: p = 0 @ x = 0
p[:,-1] = y                                     # Dirichlet BC: p = y @ x = 2
p[0,:] = p[1,:]                                 # Von Neumann BC: dp/dy = 0 @ y = 0
p[-1,:] = p[-2,:]                               # Von Neumann BC: dp/dy = 0 @ y = 1

### Main loop: define 2 functions

def plot2D(x, y, p):
    fig = pyplot.figure(figsize = (11, 7), dpi = 100)
    ax = fig.add_subplot(projection = '3d')
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, p[:], rstride = 1, cstride = 1, cmap = cm.viridis,\
                            linewidth = 0, antialiased = False)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.view_init(30, 225)
    ax.set_zlabel('p')
    ax.set_ylabel('y')
    ax.set_xlabel('x')
    pyplot.show(block = True)

def Laplace2D_FL(p, y, dx, dy, l1NormTarget):
    l1Norm = 1
    pN = numpy.empty_like(p)
    startTimeFL = timeit.default_timer()
    l1NT = l1NormTarget

    while l1Norm > l1NormTarget:
        pN = p.copy()
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                p[i,j] = ((dy**2)*(p[i+1,j]+p[i-1,j])+(dx**2)*(p[i,j+1]+p[i,j-1]))\
                        /(2*(dx**2+dy**2)) 
                
                p[:,0] = 0
                p[:,-1] = y
                p[0,:] = p[1,:]
                p[-1,:] = p[-2,:]

                l1Norm = (numpy.sum(numpy.abs(p[:])-numpy.abs(pN[:])))/(numpy.sum(numpy.abs(pN[:])))
    
    

    print("For-loop calculation complete...\nCalculation time for a norm target of",l1NT,"is",timeit.default_timer() - startTimeFL,"[s].\n")

    #return p

def Laplace2D_AO(p, y, dx, dy, l1NormTarget):
    l1Norm = 1
    pN = numpy.empty_like(p)
    
    startTimeAO = timeit.default_timer()
    l1NT = l1NormTarget

    while l1Norm > l1NormTarget:
        pN = p.copy()
        p[1:-1,1:-1] = (dy**2*(pN[1:-1,2:]+pN[1:-1,0:-2])\
                    +dx**2*(pN[2:,1:-1]+pN[0:-2,1:-1]))/(2*(dx**2+dy**2))
                
        p[:,0] = 0
        p[:,-1] = y
        p[0,:] = p[1,:]
        p[-1,:] = p[-2,:]

        l1Norm = (numpy.sum(numpy.abs(p[:])-numpy.abs(pN[:])))/(numpy.sum(numpy.abs(pN[:])))
    
    

    print("Array operation calculation complete...\nCalculation time for a norm target of",l1NT,"is",timeit.default_timer() - startTimeAO,"[s].\n")

    #return p




                
