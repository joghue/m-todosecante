# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:40:52 2021

@author: joaqu
"""

import condicoes as cond
import math
import matplotlib.pyplot as plt
import numpy as np
from grafico import triplot
from MS_Caso_convexo import Sol_convex
from grafico import plot_solucao, teste
from grafico import Analise_tri
# exemplo de lista dos triangulos lista=[[y,0 [x_1,y_1],[x_2,y_2]],[[x'_0,y'_0],[x'_1,y'_1],[x'_2,y'_2]],[[x''_0,y''_0],[x''_1,y''_1],[x''_2,y''_2]]
LT_1=[1,[2,3],[4,7]]
lt_fixo_1 = [[[12,13],[15,16],[18,19]],[[20,21],[12,14],[18,20]]]
a,b,c,d,e,f= Sol_convex(1.8, 1, cond.intmax,cond.tol1,cond.tol3,LT_1,lt_fixo_1)
print(a)
print(a)
Analise_tri(c,e)
file_name = "resultado.Tri[0].tex"
# Analise_tri(c,e)

# mtri(x,y,triangulation)
# plt.triplot(mtri)
# plt.show()