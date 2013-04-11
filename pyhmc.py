#! /usr/bin/env python2

import argparse
import math
import numpy as np
import bivariatenormal
from iterate import sample

parser = argparse.ArgumentParser()
parser.add_argument("demo", choices=["demo"], nargs="?")
parser.add_argument("likelihood", nargs="?", choices=["normal", "binomial"])
parser.add_argument("-S", type=int, help="number of samples (default 1000)")
parser.add_argument("-L", type=int,
        help="number of leapfrog steps (default 50")
parser.add_argument("-E", "--epsilon", type = float,
        help="time step (default 0.5)")
parser.add_argument("-Y", type = float, nargs="+",
        help="Data. Structure depends on likelihood")
parser.add_argument("-I", type=float, nargs="+",
        help="Chain beginning for parameters")
parser.add_argument("-V", action="store_true",
        help="Be verbose")
parser.add_argument("-O", help="Output file")


args = parser.parse_args()

if args.S:
	S = args.S
else:
	S = 1000

if args.L:
	L = args.L
else:
	L = 10

if args.epsilon:
	epsilon = args.epsilon
else:
	epsilon = 0.1

if args.Y:
	y = np.array(args.Y)
else:
	y = np.array([0, 0])

if args.demo == "demo":
	sampler = bivariatenormal.bivariateNormal()
else:
	print("I don't know that sampler")

if args.I:
	init = np.array(args.init)
else:
	init = sampler.init

if args.V:
	verbose = True
else:
	verbose = False

if args.O:
	output = args.O
else:
	output = "output.txt"

###################
#  print options  #
###################

print("\n**********************************\n")
if not args.demo=="demo":
	print("Likelihood: %s" % args.likelihood)
	print("Prior: %s" % args.prior)
if args.demo=="demo":
	print("Demo mode: Sampling from a bivariate normal \
with mean %s and standard deviation 1" % y)

print("  Number of samples: %s" % S)
print("  Steps between each sample: %s" % L)
print("  Time step size: %s" % epsilon)









qm = sample(y, S, L, epsilon, init, sampler, verbose)

np.savetxt(output, qm, delimiter=" ")

