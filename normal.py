# Sampler class of single variate normal

import math
import numpy as np

class normal:
	ldim = 2 # dimensionality
	defaulty = np.array([1, 2, 2, 1]) # default data if not given
	init = np.array([0, 2]) # default intial conditions
	pmu = [0, 0] # mean of momentum kicks
	psig = [[1, 0], [0, 1]] # covariance of momentum kicks
	ll = True # is density calculated as loglikelihood

	def readdata(self, fname):
		fh = open(fname, "r")
		y = []
		for x in fh:
			x = float(x)
			y.append(x)
		return(np.array(y))


	# probability density
	def density(self, q, y):
		sig = math.exp(q[1])
		n = len(y)
		d = np.zeros(n)
		loglik = 0
		for i in range(n):
			d[i] = q[0] - y[i]
			loglik += - d[i] ** 2. / (2. * sig ** 2.)
		loglik += - n / 2 * math.log(sig ** 2 * 2 * math.pi)
		# if loglik < -20:
			# loglik = -20
		return(loglik)

	# Calculate the derivative of the potential field
	def deriv(self, q, y):
		# one variable so going to go numerically
		h1 = np.array([0.05, 0.])
		h2 = np.array([0., 0.05])
		deltax = - (self.density(q - h1, y)) + \
				(self.density(q + h1, y))
		deltay = - (self.density(q - h2, y)) + \
				(self.density(q + h2, y))
		return(np.array([deltax / np.linalg.norm(h1),
			             deltay / np.linalg.norm(h2)]))

	def transform(self, q):
		q0 = q[0]
		q1 = math.log(q[1])
		return(np.array([q0, q1]))

	def itransform(self, q):
		q0 = q[0]
		if q[1] > 10:
			q1 = 10
		else:
			q1 = q[1]
		q1 = math.exp(q1)
		return(np.array([q0, q1]))

