# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:56:43 2019

@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

x=np.linspace(-10,10,2000)
r=np.linspace(0,5,2000)
r1=r
R1,R=np.meshgrid(r1,r)
y=x
XX,YY=np.meshgrid(x,y)
ZZ=np.cos(R*XX**1)#+np.sin(YY**1)
fig=plt.figure()
axes=Axes3D(fig)
axes.plot_surface(XX,YY,ZZ,cmap='rainbow')
plt.show()