# simple python script to check input data
#
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

import mds

import sys

# Read from standard in
nel=0
vals=list()
for line in sys.stdin:
 print float(line)
 vals.append(float(line))

plt.plot(vals)
plt.show()
