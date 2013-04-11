#! /usr/bin/env python2

import argparse
import math
import numpy as np
import sys

import bivariatenormal
from iterate import sample

# {{{ parse

parser = argparse.ArgumentParser()

# specifying the sampler
## demo -- just sample from a bivariate normal
parser.add_argument("--demo", action="store_true",
        help="Sample from a bivariate normal in demo mode")
## likelihood
parser.add_argument("likelihood", nargs="?", choices=["normal", "binomial"],
        metavar="likelihood")
## prior
parser.add_argument("prior", nargs="?", choices=["flat1", "flat2"],
        metavar="prior")

# sampler parameters
## number of samples
parser.add_argument("-S", type=int, help="number of samples", default=1000)
## number of itegrator steps
parser.add_argument("-L", type=int, help="number of integrator steps",
		default=10)
## time step
parser.add_argument("-E", "--epsilon", type = float, help="time step",
		default=0.1)
## initialize the chain
parser.add_argument("-I", type=float, nargs="+",
        help="Chain beginning for transformed parameters")

# inputs
## the data specific to the sampler type
parser.add_argument("-Y", type = float, nargs="+",
        help="Data. Structure depends on likelihood")

# outputs
## output file
parser.add_argument("-O", help="Output file", default="output.txt")

# additional options
## verbosity (for trouble shooting)
parser.add_argument("-V", action="store_true", help="Be verbose")

args = parser.parse_args()
try:
	if not (args.demo or args.likelihood):
		raise Exception
except:
	print("Either demo needs to be turned on" +
	" or likelihood and prior need to be set\n")
	parser.print_help()
	sys.exit(1)

try:
	if not args.demo:
		raise Exception
	else:
		sampler = bivariatenormal.bivariateNormal()
except:
	print("Currently, only the demo is available\n")
	parser.print_help()
	sys.exit(1)

# set run parameters
## number of samples
S = args.S
L = args.L
epsilon = args.epsilon

# set data
if args.Y:
	y = np.array(args.Y)
else:
	y = sampler.defaulty

# initialize chain
if args.I:
	init = np.array(args.init)
else:
	init = sampler.init

# verbosity
verbose = args.V

# output file
outfile = args.O

# }}}

###################
#  print options  #
###################

print("\n")
if not args.demo=="demo":
	print("Likelihood: %s" % args.likelihood)
	print("Prior: %s" % args.prior)
if args.demo=="demo":
	print("Demo mode: Sampling from a bivariate normal \
with mean %s and standard deviation 1" % y)

print("  Number of samples: %s" % S)
print("  Steps between each sample: %s" % L)
print("  Time step size: %s" % epsilon)

print("\nWriting results to %s" % outfile)



######################
#  Perform sampling  #
######################

qm = sample(y, S, L, epsilon, init, sampler, verbose)



#################
#  save output  #
#################

np.savetxt(outfile, qm, delimiter=" ")

# vim:foldmethod=marker
