# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:03:42 2021

@author: joaqu
"""
from sympy import Symbol, factor, pprint
from funcpython import sec
import condicoes as cond
import math

from scipy.optimize import minimize
def tri(y,l_1,l_2,alpha,vertice_4,vertice_5,vertice_6):
    a =Symbol('a')
    b = Symbol('b')
    y_2 = y + l_1*math.cos(alpha)
    y_3 = y + l_2*math.cos(alpha)
    return lambda x:max(x*a + y*b,  (x +  l_1*math.sin(alpha))*a + y_2*b,x +  l_2*math.sin(alpha)*a + y_3*b ) - min(vertice_4[0]*a + vertice_4[1]*b, vertice_5[0]*a + vertice_5[1]*b, vertice_6[0]*a + vertice_6[1]*b)
def triangulo(vertice_1, vertice_2,vertice_3,vertice_4,vertice_5,vertice_6,x_2):
  return lambda x_1: x_1
i=1

vertice_1 = [1,2]
vertice_2 = [3,4]
vertice_3 = [5,6]
vertice_4 = [11,12]
vertice_5 = [13,14]
vertice_6 = [15,16]
Solution,Count,tuplex,error,funcoes,e = sec(tri(1,2,3,0.3,[11,12],[13,14],[15,16]),2,3,cond.intmax,cond.tol1,cond.tol3)
print(Solution)
print(Count)
u = 0
if u == 1:
 while max(vertice_1[0]*Solution + vertice_1[1]*i, vertice_2[0]*Solution + vertice_2[1]*i, vertice_3[0]*Solution + vertice_3[1]*i )> min(vertice_4[0]*Solution + vertice_4[1]*i, vertice_5[0]*Solution + vertice_5[1]*i, vertice_6[0]*Solution + vertice_6[1]*i) and max(abs(Solution),abs(i))>= 1:
    i = i +2
    Solution,Count,tuplex,error,funcoes,e = sec(triangulo([1,2],[3,4],[5,6],[11,12],[13,14],[15,16],i),2,3,cond.intmax,cond.tol1,cond.tol3)
    
    
    if max(vertice_1[0]*Solution + vertice_1[1]*i, vertice_2[0]*Solution + vertice_2[1]*i, vertice_3[0]*Solution + vertice_3[1]*i )< min(vertice_4[0]*Solution + vertice_4[1]*i, vertice_5[0]*Solution + vertice_5[1]*i, vertice_6[0]*Solution + vertice_6[1]*i ) and max(abs(Solution),abs(i))>= 1:
        print("not overlapping")
        print(i)
        print(Solution)
    else:
        print(" sobrepostos")
        continue
