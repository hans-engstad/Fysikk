# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:21:23 2020

@author: Marius
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

yfast = [0.293, 0.24, 0.216, 0.159, 0.082, 0.053, 0.097, 0.136]
xfast = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]

# y(x)
cs = CubicSpline(xfast, yfast, bc_type="natural")
xmin = 0.000
xmax = 1.401
dx = 0.001
x = np.arange(xmin, xmax, dx)
Nx = len(x)
y = cs(x)
dy = cs(x, 1)
d2y = cs(x, 2)


# Plotting

# baneform = plt.figure('y(x)',figsize=(12,3))
# plt.plot(x,y,xfast,yfast,'*')
# plt.title('Banens form')
# plt.xlabel('$x$ (m)',fontsize=20)
# plt.ylabel('$y(x)$ (m)',fontsize=20)
# plt.ylim(0,0.350)
# plt.grid()
# plt.show()

# helningsvinkel
beta = np.arctan(dy)

# baneform = plt.figure('B',figsize=(12,3))
# plt.plot(x,beta)
# plt.title('Banens helningsvinkel')
# plt.xlabel('$x$ (m)',fontsize=20)
# plt.ylabel('$Beta$ (grader)',fontsize=20)
# plt.ylim(-1/2,1/2)
# plt.grid()
# plt.show()


# Hastighet
speed = []
for i in y:
    speed.append(np.sqrt((2 * (9.81) * (yfast[0] - i)) / (1.5)))

# baneform = plt.figure('Hastighet',figsize=(12,3))
# plt.plot(x,speed)
# plt.title('Hastighet')
# plt.xlabel('$x$ (m)',fontsize=20)
# plt.ylabel('$Hastighet$ (m/s)',fontsize=20)
# plt.ylim(0,2.5)
# plt.xlim(0,1.5)
# plt.grid()
# plt.show()

# Krumning

K = []
for i in range(len(y)):
    K.append(d2y[i] / (1 + dy[i] ** 2) ** (3 / 2))

# baneform = plt.figure('Kruming',figsize=(12,3))
# plt.plot(x,K)
# plt.title('Kruming')
# plt.xlabel('$x$ (m)',fontsize=20)
# plt.ylabel('$K$ (1/m)',fontsize=20)
# plt.ylim(-2,3)
# plt.xlim(0,1.5)
# plt.grid()
# plt.show()

