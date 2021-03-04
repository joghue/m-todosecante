# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:36:44 2020

@author: joaqu
"""
"""arquivo principal dos problemas envolvendo circuferencia"""
# bibliotecas importadas
from funcpython import sec 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
from grafico import plot_solucao,plot_erro,plot_analise,teste, teste_2
import listas as lt
import funccirc as fc
import condicoes as cond
import feradores as fe
# função 
i = 0
file_name = ("resultado[i].txt")
print(file_name)
with open(file_name,"w") as file_object:
  for i in range(0,6):
    Solution,Count,tuplex,error,funcoes = sec(fc.circ_1,fe.intervalos[i],fe.intervalos[i+1],cond.intmax,cond.tol1,cond.tol3) 
    condicao = 1
    k = len(tuplex) 
    j = 0
    DesvioPadrão = np.std(tuplex, axis = 0, dtype = float)
    print(Solution)
    A_1 = str(fe.intervalos[i])
    A_2 = str(fe.intervalos[i+1])  
    A = str(Solution)
    B = str(Count)
    C = str(tuplex)
    D = str(DesvioPadrão)
    a = (A_1 + "&" + A_2 + "&"+ A + "& " + B + "& "+ C + "& " + D  + "\n"  )
    file_object.write(a)
    
  
    