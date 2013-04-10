#! /usr/bin/env python2

import argparse
import math
import numpy as np
from iterate import sample

# parser = argparse.ArgumentParser()
# parser.add_argument("likelihood", help="help on likelihood")
# args = parser.parse_args()
# print args.likelihood

B = True

if B:
	from bivariatenormal import *


# number of leapfrog steps
L = 50
# step size
epsilon = 0.5
# number of samples
S = 100


qm = sample(S, L, epsilon, [3, 0], density, deriv)

qm = transform(qm)

np.savetxt("./output/output.txt", qm, delimiter=" ")

