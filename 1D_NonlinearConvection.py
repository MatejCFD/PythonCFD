import numpy, decimal
from matplotlib import pyplot
import time, sys

nx = 101
dx = 2/(nx-1)
nt = 100
dt = 0.0025

u = numpy.ones(nx)
k = numpy.linspace(0,1,11)
L = len(k)

for j in range(L):
    u[int(0.5/dx):int(1/dx + 1)] = k[j]

    un = numpy.ones(nx)
    for i in range(nt):
        un = u.copy()
        for i in range(nx):
            u[i] = un[i] - un[i]*(dt/dx)*(un[i]-un[i-1])

    print(u)
    flag = 'k=%s' % str(round(k[j],2))
    pyplot.plot(numpy.linspace(0,2,nx),u)
    ax = pyplot.gca()
    pyplot.title("%s" % flag)
    ax.set_ylim(-0.2,1.2)
    pyplot.savefig("%s.png" % flag)
    pyplot.show(block=True)
