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
from MS_Caso_convexo import Sol_convex
from grafico import plot_solucao, teste
from secante_adulterada import Sol_Triangle
from grafico import Analise_tri
# LT_0 = [yA,l1A,l2A,z,theta,xB,yB,l1B,l2B,a1B,a2B]
LT_1 = [0,5,5,60,0,3.5,1.9,2,2,30,104]
LT_2 = [0,5,5.8,56,0,3.5,0,3.9,2,30,104]
LT_3 = [0,5,2.9,137,0,1.1,0,2.1,2,30,104]
LT_4 = [0.3,2.6,4.5,212,0,2.4,0,2.1,2,49,36]
LT_5 = [0.3,2.6,4.5,212,0,2.4,0,2.1,2,49,336]
LT_6 = [1.6,1.4,2.4,45,212,0,0,2.1,2,49,336]
LT_7 = [2.3,2.,4.5,212,0,1.6,0,2.1,2,49,336]
LT_8 = [1.3,2.9,4.7,212,0,1.6,1.7,3,2,49,300]
LT_9 = [1.9, 2.9,4.7,212,0,1,2.2,3.1,5,49,180]
# a,b,c,d,e,f= Sol_Triangle(1.8, 1, cond.intmax,cond.tol1,cond.tol3,LT_0_FIXO,LT_1)
a,b,c,d,e,f= Sol_Triangle(1.8, 1, cond.intmax,cond.tol1,cond.tol3,LT_1)
print(a)
print(a)
Analise_tri(c,e)
file_name = "resultado.Tri[0].tex"
# Analise_tri(c,e)

# mtri(x,y,triangulation)
# plt.triplot(mtri)
# plt.show()