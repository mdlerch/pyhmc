import numpy as np
import math

def logit(pi):
	logodds = math.log(pi / (1. - pi))
	return(logodds)

def ilogit(w):
	pr = math.exp(w) / (1. + math.exp(w))
	return(pr)

# density
def density(q, y):
	pdf = ilogit(q) ** y[0] * (1. - ilogit(q)) ** (y[1] - y[0])
	if pdf<= 0:
		pdf = 1E-10
	return(pdf)

# Calculate the derivative of the potential field
def deriv(q, y):
	p = ilogit(q)
	factor = (math.exp(q) / (1 + math.exp(q))) ** 2.
	out = (y[0] * 1. / p - (y[1] - y[0]) * 1. / (1. - p)) * factor
	return(out)

def itransform(w):
	return(ilogit(w))

def transform(q):
	return(logit(q))
