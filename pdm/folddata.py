# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:53:14 2020

@author: dingxu
"""

from PyAstronomy.pyasl import foldAt
import matplotlib.pylab as plt
import numpy as np
from PyAstronomy.pyTiming import pyPDM

# Generate some data ...
data = np.loadtxt('datamag.txt')
#time = np.arange(0,119,0.1)
time = data[:,0:1]-np.min(data[:,0:1])
flux = data[:,1:2]

plt.figure(0)
plt.plot(time, flux, 'bp')
# Obtain the phases with respect to some
# reference point (in this case T0=217.4)
S = pyPDM.Scanner(minVal=0.1, maxVal=120, dVal=0.001, mode="frequency")
P = pyPDM.PyPDM(time, flux)
f2, t2 = P.pdmEquiBin(20, S)
plt.figure(1)
plt.plot(f2, t2, 'bp-')
locaf2 = np.where(t2 == np.min(t2))
ylo =locaf2[0][0] 
print(f2[ylo])

phases = foldAt(time, 1/f2[ylo])

# Sort with respect to phase
# First, get the order of indices ...
sortIndi = np.argsort(phases)
# ... and, second, rearrange the arrays.
phases = phases[sortIndi]
flux = flux[sortIndi]
# Plot the result
plt.figure(2)
plt.plot(phases, flux, 'bp')
plt.show()