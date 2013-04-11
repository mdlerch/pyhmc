import numpy as np
import math

def leapfrog(q, p, y, eps, sampler):
	p2 = p + eps / 2. * sampler.deriv(q, y)
	q2 = q + eps * p2
	p2 = p2 + eps / 2. * sampler.deriv(q2, y)
	return(q2, p2)

def hamiltonian(q, p, y, sampler):
	E = - math.log(sampler.density(q, y)) + 1. / 2. *  np.dot(p, p)
	return(E)

def sample(y, S, L, eps, qi, sampler, verbose):
	qm = np.zeros([S, sampler.ldim])
	q = np.zeros([L, sampler.ldim])
	p = np.zeros([L, sampler.ldim])
	qm[0] = sampler.transform(qi)
	for i in range(S-1):
		q[0] = qm[i]
		p0 = p[L - 1]
		p[0] = np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]])

		for step in range(L-1):
			if verbose:
				print "position: %s" % q[step]
				print "momentum: %s" % p[step]

			q[step + 1], p[step + 1] = leapfrog(q[step], p[step], y, eps,
			  sampler)

		# MH acceptance/rejection
		Ei = hamiltonian(q[0], p0, y, sampler)
		Ef = hamiltonian(q[L - 1], p[L - 1], y, sampler)
		alpha = min(1, math.exp(- Ef + Ei))
		if verbose:
			print "Energy_i: %s, %s" % (Ei, q[0])
			print "Energy_f: %s" % Ef
			print "alpha: %s" % alpha
		if np.random.random() < alpha:
			qm[i + 1] = sampler.itransform(q[L - 1])
		else:
			qm[i + 1] = qm[i]
	return(qm)
