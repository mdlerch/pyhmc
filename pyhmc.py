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
L = 50
# step size
epsilon = 1.

# mass
m = 1000.

I = 10

# initialize and initial conditions

xm = np.zeros([M,2])
xm[0] = x[0]

x = np.zeros([L, 2])
v = np.zeros([L, 2])
x[L - 1] = [3, 0]
v[L - 1] = [0, .05]


for i in range(I):
	x[0] = x[L - 1]
	v[0] = np.random.multivariate_normal([0, 0], [[1,0], [0,1]]) / m
	for step in range(L-1):
		x[step + 1], v[step + 1] = leapfrog(x[step], m * v[step], epsilon, m)
	np.savetxt("outputx"+str(i)+".txt",x,delimiter=" ")

