# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:16:53 2021

@author: joaqu
"""
#gera a partir  das raízes, intervalos
import math
a,b = (-2,50)
choose = 1
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
    c = (a+b)/2 + (a-b)/2
    d = (a+b)/3 + (a-b)/2
    e = (a+b)/4 + (a-b)/2
    f= (a+b)/5 + (a-b)/2
    g= (a+b)/6 + (a-b)/2
    h = (a+b)/7 + (a-b)/2
intervalos.append(c)
intervalos.append(d)
intervalos.append(e)
intervalos.append(g)
intervalos.append(f)
intervalos.append(h)
    
   