# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:17:28 2021

@author: joaqu
"""
# Variavel x vai ser a0
# função max(v-w)**2

import numpy as np
import matplotlib.pyplot as plt
b = []
i = 0 
k= 0 

resultados = []
while(i<99):
    a = np.random.rand(1,2)
    b.append(a)
    i= i+1
vert_1 = [5.0, -7.0]
vert_2 = [7.0, -7.0]
vert_3 = [6.0, -5.0]
vert_5= [6.0, -6.0]
vert_6= [8.0, -6.0]
vert_7= [7.0, -4.0]
while(k<99):
 v = max( np.dot(b[k], vert_1), np.dot(b[k], vert_2), np.dot(b[k], vert_3) )
 h =max( np.dot(b[k], vert_5), np.dot(b[k], vert_6), np.dot(b[k], vert_7) )
 u = b[k]
 k = k +1
 print(v)
 f_n= (v-h)**2
 resultados.append(f_n)

x = list(range(0,99))
plt.grid()
plt.plot(x,resultados)
plt.show()