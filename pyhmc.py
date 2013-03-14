import math
import numpy as np
import csv

# potential
def potential(x):
	pdf = exp((x[0] - 0) ** 2 / 2) * exp((x[1] - 0) ** 2 / 2)
	return(pdf)

# hamiltonian
def hamiltonian(x, p):
	E = - math.log(potential(x)) + 1./2. * np.dot(p,p)
	return(E)



# Calculate the derivative
def deriv(x):
	dx = - x[0]
	dy = - x[1]
	out = np.array([dx, dy])
	return(out)

# Iteration
def leapfrog(x, p, eps, m):
	p2 = p + eps / 2. * deriv(x)
	x2 = x + eps * p2 / m
	p2 = p2 + eps / 2. * deriv(x2)
	v2 = p2 / float(m)
	return( x2, v2 )





# number of leapfrog steps
L = 1000
# step size
epsilon = 1.

# mass
m = 1000

# initialize and initial conditions
x = np.zeros([L, 2])
v = np.zeros([L, 2])
x[0] = [3, 0]
v[0] = [0, .05]

for step in range(L-1):
	x[step + 1], v[step + 1] = leapfrog(x[step], m * v[step], epsilon, m)


np.savetxt("outputx.txt",x,delimiter=" ")
np.savetxt("outputv.txt",v,delimiter=" ")
