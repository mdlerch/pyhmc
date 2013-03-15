import math
import numpy as np
import csv

# density
def density(x):
	pdf = math.exp((x[0] - 0) ** 2 / 2) * math.exp((x[1] - 0) ** 2 / 2)
	return(pdf)

# hamiltonian
def hamiltonian(x, v, m):
	E = - math.log(density(x)) + 1./2. * m * np.dot(v, v)
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
m = 20.

I = 5000

# initialize and initial conditions

xm = np.zeros([I,2])

x = np.zeros([L, 2])
v = np.zeros([L, 2])
x[L - 1] = [3, 0]
v[L - 1] = [0, .05]


for i in range(I-1):
	x[0] = x[L - 1]
	v0 = v[L -1]
	v[0] = np.random.multivariate_normal([0, 0], [[1,0], [0,1]]) / m
	for step in range(L-1):
		x[step + 1], v[step + 1] = leapfrog(x[step], m * v[step], epsilon, m)

	Ei = hamiltonian(x[0], v0, m)
	Ef = hamiltonian(x[L-1], v[L-1], m)

	alpha = min(1, math.exp(- Ef + Ei))

	if np.random.random() < alpha:
		xm[i + 1] = x[L - 1]
	else:
		xm[i + 1] = xm[i]

	# np.savetxt("outputx"+str(i)+".txt",x,delimiter=" ")

np.savetxt("output.txt", xm, delimiter=" ")

