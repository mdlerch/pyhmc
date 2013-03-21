import numpy as np
from iterate import sample



# number of leapfrog steps
L = 50
# step size
epsilon = 0.5
# number of samples
S = 10000

qm = sample(S, L, epsilon, [3,0])

np.savetxt("./output/output.txt", qm, delimiter=" ")

