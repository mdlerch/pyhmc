import numpy as np
import math

# density
def density(x):
	pdf = math.exp((x[0] - 0) ** 2 / 2) * math.exp((x[1] - 0) ** 2 / 2)
	return(pdf)

# hamiltonian
def hamiltonian(x, v, m):
	E = - math.log(density(x)) + 1./2. * m * np.dot(v, v)
	return(E)

# Calculate the derivative of the potential field
def deriv(x):
	dx = - x[0]
	dy = - x[1]
	out = np.array([dx, dy])
	return(out)
