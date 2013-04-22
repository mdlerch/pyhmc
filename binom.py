# Sampler class of binomial

import math
import numpy as np

class binomial:
	ldim = 1 # dimensionality
	defaulty = np.array([1, 2]) # default data if not given
	init = np.array([.5]) # default intial conditions
	pmu = 0 # mean of momentum kicks
	psig = 1 # covariance of momentum kicks

	def readdata(self, fname):
		fh = open(fname)
		n = 0
		y = 0
		for x in fh:
			x = float(x[0])
			if not (x==1 or x==0):
				raise Exception("input data issues")
			n+=1
			y+=x
		return [y, n]



	# probability density
	def density(self, q, y):
		mult = math.exp(q) / (1. + math.exp(q)) ** 2
		return(self.itransform(q) ** y[0] *
		       (1. - self.itransform(q)) ** (y[1] - y[0]) * mult)

	# Calculate the derivative of the potential field
	def deriv(self, q, y):
		# one variable so going to go numerically
		h = .05
		delta = self.density(q - h, y) - self.density(q + h, y)
		return(delta/(2 * h))

	def transform(self, q):
		if (q < 1E-5):
			q = 0.001
		return(math.log(q / (1. - q)))

	def itransform(self, w):
		return(math.exp(w) / (1. + math.exp(w)))

