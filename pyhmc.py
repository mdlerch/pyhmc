#! /usr/bin/env python2

import argparse
import math
import numpy as np
import sys

import bivariatenormal
import binom
from iterate import sample

# {{{ parse

parser = argparse.ArgumentParser()

# specifying the sampler
## demo -- just sample from a bivariate normal
parser.add_argument("--demo",
                    action="store_true",
                    help="Sample from a bivariate normal in demo mode")
## likelihood
parser.add_argument("likelihood",
                    nargs="?",
                    choices=["binomial"],
                    metavar="likelihood",
                    help="Likelihood to use")
## prior
# parser.add_argument("prior",
                    # nargs="?",
                    # choices=["flat1", "flat2"],
                    # metavar="prior",
                    # help="prior to use")

# sampler parameters
## number of samples
parser.add_argument("-S",
                    type=int,
                    default=1000,
                    help="number of samples")
## number of itegrator steps
parser.add_argument("-L",
                    type=int,
                    default=10,
                    help="number of integrator steps between samples")
## time step
parser.add_argument("-E",
                    "--epsilon",
                    type = float,
                    default=0.1,
                    help="time step")
## initialize the chain
parser.add_argument("-I",
                    type=float,
                    nargs="+",
                    help="Chain beginning for canonical parameters")

# inputs
## the data specific to the sampler type
parser.add_argument("-Y",
                    type = float,
                    nargs="+",
                    help="Data. Structure depends on likelihood")

parser.add_argument("--infile",
                    nargs="+",
                    help="Data. Structure depends on likelihood")
# outputs
## output file
parser.add_argument("-O",
                    default="output.txt",
                    help="Output file")

# additional options
## verbosity (for trouble shooting)
parser.add_argument("-V",
                    action="store_true",
                    help="Be verbose")


args = parser.parse_args()

try:
	if not (args.demo or args.likelihood):
		raise Exception
except:
	print("Either demo needs to be turned on" +
	" or likelihood needs to be set\n")
	parser.print_help()
	sys.exit(1)

######################################
#  Only demo is currently available  #
######################################

try:
	if not args.demo:
		if args.likelihood == "binomial":
			sampler = binom.binomial()
		else:
			raise Exception
		pass
except:
	print("Currently only binomial is available\n" +
			"you selected %s" % args.likelihood)
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

if args.infile:
	y = sampler.readdata(args.infile[0])

# initialize chain
if args.I:
	init = transform(np.array(args.init))
else:
	init = sampler.init

# verbosity
verbose = args.V

# output file
outfile = args.O

# }}}

# {{{ print options

print("\n")
if not args.demo=="demo":
	print("Likelihood: %s" % args.likelihood)
	# print("Prior: %s" % args.prior)
if args.demo=="demo":
	print("Demo mode: Sampling from a bivariate normal \
with mean %s and standard deviation 1" % y)

print("  Number of samples: %s" % S)
print("  Steps between each sample: %s" % L)
print("  Time step size: %s" % epsilon)

print("\nWriting results to %s" % outfile)

# }}}

######################
#  Perform sampling  #
######################

qm = sample(y, S, L, epsilon, init, sampler, verbose)


#################
#  save output  #
#################

np.savetxt(outfile, qm, delimiter=" ")

# vim:foldmethod=marker
