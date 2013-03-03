import math
import numpy as np
import csv

def deriv(pos):
	# dx = - x[0] * math.exp(- x[0] ** 2 / 2) * math.exp(- x[1] ** 2 / 2)
	# dy = - x[1] * math.exp(- x[1] ** 2 / 2) * math.exp(- x[0] ** 2 / 2)
	dx = - pos[0]
	dy = - pos[1]
	out = np.array([dx, dy])
	return(out)

L = 1000
epsilon = 1

m = 1000

x = np.zeros([L, 2])
v = np.zeros([L, 2])

x[0] = [3, 0]
v[0] = [0, .05]

for step in range(L-1):
	x[step + 1] = x[step] + epsilon * v[step]
	v[step + 1] = v[step] + epsilon * deriv(x[step])/m


np.savetxt("outputx.txt",x,delimiter=" ")
np.savetxt("outputv.txt",v,delimiter=" ")
