import numpy
from matplotlib import pyplot
import time, sys

nx = 41
nt = 25
dx = 2/(nx-1)
dt = 0.0025
nu = numpy.linspace(0,0.3,31)
L = len(nu)

u = numpy.ones(nx)
un = numpy.ones(nx)

for j in range(L):
    u[int(0.5/dx):int(1/dx+1)] = nu[j]
    for i in range(nt):
        un = u.copy()

        for i in range(nx-1):
            u[i] = un[i] + nu[j]*dt/((dx)**2)*(un[i+1]-2*un[i]+un[i-1])

    print(u)
    flag = "nu=%s" % str(round(nu[j],2))
    fflag = "nu %s" % str(j)
    pyplot.plot(numpy.linspace(0,2,nx),u)
    ax = pyplot.gca()
    ax.set_ylim(0,1.2)
    ax.set_xlim(0,2)
    pyplot.title("%s" % flag)
    pyplot.savefig("%s.png" % fflag)
    pyplot.show(block=True)

