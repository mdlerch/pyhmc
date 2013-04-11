import math
import numpy as np

class bivariateNormal:
	ldim = 2
	init = np.array([10, 10])

	# density
	def density(self, q, y):
		pdf = math.exp(-(q[0] - y[0]) ** 2. / 2.) * math.exp(-(q[1] - y[1]) ** 2. / 2.)
		return(pdf)

	# Calculate the derivative of the potential field
	def deriv(self, q, y):
		dx = - q[0] + y[0]
		dy = - q[1] + y[1]
		out = np.array([dx, dy])
		return(out)

	# transformation to original scale
	def transform(self, q):
		return(q)

	def itransform(self, q):
		return(q)
