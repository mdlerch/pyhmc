import math
import numpy as np
from iterate import sample

B = True

if B:
	from bivariatenormal import *


# number of leapfrog steps
L = 50
# step size
epsilon = 0.5
# number of samples
S = 100


qm = sample(S, L, epsilon, [3,0], density, deriv)

qm = transform(qm)

np.savetxt("./output/output.txt", qm, delimiter=" ")

