# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-np.pi,np.pi,256,endpoint=True)
(C,S) = np.cos(X),np.sin(X)  #linspace在（-pi,pi)之间分成共256个小段，并把这256个值赋给X
plt.plot(X,C)
plt.plot(X,S)