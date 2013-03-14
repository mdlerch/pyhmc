import math
import numpy as np
import csv

# Calculate the derivative
def deriv(x):
	# dx = - x[0] * math.exp(- x[0] ** 2 / 2) * math.exp(- x[1] ** 2 / 2)
	# dy = - x[1] * math.exp(- x[1] ** 2 / 2) * math.exp(- x[0] ** 2 / 2)
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
	return x2, v2



# number of leapfrog steps
L = 1000
epsilon = 1.

m = 1000

x = np.zeros([L, 2])
v = np.zeros([L, 2])
xl = np.zeros([L, 2])
vl = np.zeros([L, 2])

x[0] = [3, 0]
v[0] = [0, .05]
xl[0] = [3, 0]
vl[0] = [0, .05]

for step in range(L-1):
	xl[step + 1], vl[step + 1] = leapfrog(xl[step], m * vl[step], epsilon, m)
	x[step + 1] = x[step] + epsilon * v[step]
	v[step + 1] = v[step] + epsilon * deriv(x[step])/m


np.savetxt("outputx.txt",x,delimiter=" ")
np.savetxt("outputv.txt",v,delimiter=" ")
np.savetxt("outputxl.txt",xl,delimiter=" ")
np.savetxt("outputvl.txt",vl,delimiter=" ")
