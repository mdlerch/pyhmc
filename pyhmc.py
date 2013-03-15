import math
import numpy as np
import csv
from bivariatenormal import *

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

# number of momentum kicks
I = 5000

# initialize and initial conditions

# samples
xm = np.zeros([I,2])

# leapfrog sequence
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

	# gibbs acceptance/rejection
	Ei = hamiltonian(x[0], v0, m)
	Ef = hamiltonian(x[L-1], v[L-1], m)
	alpha = min(1, math.exp(- Ef + Ei))
	if np.random.random() < alpha:
		xm[i + 1] = x[L - 1]
	else:
		xm[i + 1] = xm[i]

	# np.savetxt("./output/outputx"+str(i)+".txt",x,delimiter=" ")

np.savetxt("./output/output.txt", xm, delimiter=" ")

