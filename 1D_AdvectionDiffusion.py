import numpy
from matplotlib import pyplot
import time, sys
import sympy
from sympy.utilities.lambdify import lambdify


x, nu, t = sympy.symbols('x nu t')                      # Define symbolic variables
phi = (sympy.exp(-(x-4*t)**2/(4*nu*(t+1)))+             # Define function phi symbolically
       sympy.exp(-(x-4*t-2*sympy.pi)**2/(4*nu*(t+1))))
#print(phi)

phiPrime = phi.diff(x)                                  # Differentiate phi with respect to x
#print(phiPrime)

u = -2*nu*(phiPrime/phi) + 4                            # Define IC, in this case SOLUTION
#print(u)

uFunc = lambdify((t, x, nu), u)                         # Turn a symbolic expression into a 
                                                        # useful/callable function
nx = 101                                                # Grid points
nt = 100                                                # Time points
dx = 2*numpy.pi/(nx-1)                                  # [m] Grid size
nu = 0.07                                               # [Pa*s] Dynamic viscosity
dt = dx*nu                                              # [s] Timestep

x = numpy.linspace(0, 2*numpy.pi, nx)                                   
un = numpy.empty(nx)
t = 0

u = numpy.asarray([uFunc(t, x0, nu) for x0 in x])       # values of u @ t = 0, for all x0 in x
#print(u)

pyplot.figure(figsize = (11, 7), dpi = 100)
pyplot.plot(x, u, marker = 'o', lw = 2)
pyplot.xlim([0, 2*numpy.pi])
pyplot.ylim([0, 10])
pyplot.show(block = True)

for n in range(nt):
    un = u.copy()
    for i in range(nx-1):
        u[i] = un[i]-un[i]*dt/dx*(un[i]-un[i-1])+nu*dt/((dx)**2)*(un[i+1]-2*un[i]+un[i-1])
    u[0] = un[0]-un[0]*dt/dx*(un[0]-un[-2])+nu*dt/((dx)**2)*(un[1]-2*un[0]+un[-2])
    u[-1] = un[0]                                       # BC: u(x0,t) = u(xLast,t)

uAnalytical = numpy.asarray([uFunc(nt*dt, xi, nu) for xi in x])
print(uAnalytical)
print(u)

pyplot.figure(figsize = (11, 7), dpi = 100)
pyplot.plot(x, u, marker = 'o', lw = 2, label = 'Computational')
pyplot.plot(x, uAnalytical, label = 'Analytical')
pyplot.xlim([0, 2*numpy.pi])
pyplot.ylim([0, 10])
pyplot.legend()
pyplot.show(block = True)

