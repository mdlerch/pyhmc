import numpy as np
import math

# density
def density(q):
	pdf = math.exp((q[0] - 0) ** 2 / 2) * math.exp((q[1] - 0) ** 2 / 2)
	return(pdf)

# hamiltonian
def hamiltonian(q, p):
	E = - math.log(density(q)) + 1./2. *  np.dot(p, p)
	return(E)

# Calculate the derivative of the potential field
def deriv(q):
	dx = - q[0]
	dy = - q[1]
	out = np.array([dx, dy])
	return(out)
