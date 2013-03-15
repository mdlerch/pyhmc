import numpy as np
import math

def logit(pi):
	logodds = math.log(pi/(1-pi))
	return(logodds)

def ilogit(w):
	pr = math.exp(w) / (1 + math.exp(w))
	return(pr)

# density
def density(q):
	pdf = ilogit(q) ** k * (1 - ilogit(q)) ** (n-k)
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
