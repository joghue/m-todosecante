# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:16:53 2021

@author: joaqu
"""
#gera a partir  das raízes, intervalos
import math
a,b = (3,-3.86383)
choose = 0
intervalos = []
if(choose == 1):

    c = a - (2)*b
    d= a - b
    e = a + (1/2)*b
    g = a + (5/6)*b
    f= a + 3*b
    h= a +(4)*b
    intervalos.append(c)
    intervalos.append(d)
    intervalos.append(e)
    intervalos.append(g)
    intervalos.append(f)
    intervalos.append(h)
    print(intervalos)
else:
    c = -2*a
    d = -3*a
    e = 2*a
    f= 3*a
intervalos.append(c)
intervalos.append(d)
intervalos.append(e)
intervalos.append(f)
    
   