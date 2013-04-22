# Sampler class of bivariate normal
# This is for demo mode, simply sample from a bivariate normal distribution


import math
import numpy as np

class bivariateNormal:
	ldim = 2 # dimensionality
	defaulty = np.array([0, 0]) # default data if not given
	init = np.array([10, 10]) # default intial conditions
	pmu = [0, 0] # mean of momentum kicks
	psig = [[1, 0], [0, 1]] # covariance of momentum kicks
	ll = False # is density calculated on log scale?

	# probability density
	def density(self, q, y):
		d0 = q[0] - y[0]
		d1 = q[1] - y[1]
		pdf = math.exp(- d0 ** 2. / 2.) * math.exp(- d1 ** 2. / 2.)
		return(pdf)

	# Calculate the derivative of the potential field
	def deriv(self, q, y):
		dx = - q[0] + y[0]
		dy = - q[1] + y[1]
		out = np.array([dx, dy])
		return(out)

	## transformations are trivial here but not for other types like binomial
	# transformation to original scale
	def transform(self, q):
		return(q)

	def itransform(self, q):
		return(q)

