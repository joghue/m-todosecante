# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:00:21 2021

@author: joaqu
"""

import condicoes as cond
import math
import matplotlib.pyplot as plt
import numpy as np
from grafico import triplot
from grafico import plot_solucao, teste
from secante_adulterada import Sol_convex
from grafico import Analise_tri
# LT_0 = [yA,l1A,l2A,z,theta,xB,yB,l1B,l2B,a1B,a2B]
LT_1=[1,[2,3],[4,7],[12,13],[15,16],[18,19]]
# a,b,c,d,e,f= Sol_Triangle(1.8, 1, cond.intmax,cond.tol1,cond.tol3,LT_0_FIXO,LT_1)
a,b,c,d,e,f= Sol_convex(0, 1, cond.intmax,cond.tol1,cond.tol3,LT_1)
print(a)


fig = plt.figure()
ax = plt.axes(projection='3d')
# Analise_tri(c,e)
file_name = "resultado.Tri[0].tex"
# Analise_tri(c,e)

# mtri(x,y,triangulation)
# plt.triplot(mtri)
# plt.show()