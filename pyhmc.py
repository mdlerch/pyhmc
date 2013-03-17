import math
import numpy as np
import csv
from bivariatenormal import *

# Iteration
def leapfrog(q, p, eps):
	p2 = p + eps / 2. * deriv(q)
	q2 = q + eps * p2
	p2 = p2 + eps / 2. * deriv(q2)
	return(q2, p2)

# number of leapfrog steps
L = 50
# step size
epsilon = 0.5

# mass
m = 20.

# number of momentum kicks
I = 5000

# initialize and initial conditions

# samples
qm = np.zeros([I,2])

# leapfrog sequence
q = np.zeros([L, 2])
p = np.zeros([L, 2])
qm[0] = [3, 0]

for i in range(I-1):
	q[0] = qm[i]
	p0 = p[L -1]
	p[0] = np.random.multivariate_normal([0, 0], [[1,0], [0,1]])

	for step in range(L-1):
		q[step + 1], p[step + 1] = leapfrog(q[step], p[step], epsilon)

	# gibbs acceptance/rejection
	Ei = hamiltonian(q[0], p0)
	Ef = hamiltonian(q[L-1], q[L-1])
	alpha = min(1, math.exp(- Ef + Ei))
	if np.random.random() < alpha:
		qm[i + 1] = q[L - 1]
	else:
		qm[i + 1] = qm[i]

	# np.savetxt("./output/outputx" + str(i) + ".txt", q, delimiter=" ")


np.savetxt("./output/output.txt", qm, delimiter=" ")

