# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:25:38 2020

@author: joaqu
"""
"""arquivo para experimentação e modelagem"""
def quadrado(lista):
    return lambda x:max(0,abs(x+lista[1]-lista[0]))*max(0,abs(lista[0]+lista[1]-x))

import numpy as np
import condicoes as cd
import math
import grafico as gr
from funcpython import sec 


lista_0=[3,4]
lista_1=[3,12]
lista_2=[2,33]
lista_3 = [-1,15]
lista_4 = [0,22]
lista_5 = [-3,11]
lista_6 =  [-4,11]
lista_7=[-2,16]
lista_8 = [2,55]
lista_9 = [-2,52]
Solution,Count,tuplex,error = sec(quadrado(lista_2),cd.initial,cd.second,cd.tol1,cd.intmax,cd.tol3)
k = len(tuplex)
i = 0
j = 0
for i in range (0,k):
    for j in range(0,k):
        if tuplex[i] < tuplex[j]:
            temp = tuplex[i]
            tuplex[i] = tuplex[j]
            tuplex[j] = temp
        else:
            continue
DesvioPadrão = np.std(tuplex, axis = 0, dtype = float)
gr.plot_quad(lista_1,Solution,"fig")
gr.plot_Analisequad(lista_0,Solution,quadrado(lista_3),tuplex,"fig2")
gr.plot_erro(error,"fig4")
print(Solution)
print(tuplex)
print(Count)
print(error)
print(DesvioPadrão)              