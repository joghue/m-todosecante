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
import feradores as fe
import sys
import condicoes as cond
def printf(format, *args):
    sys.stdout.write(format % args)
#função 
i = 0
a = str(i)
file_name = "resultado.sqrt(10).tex"
print(file_name)
with open(file_name,"w") as file_object:
  for i in range(0,6):
    str(i)
    Solution,Count,tuplex,error,funcoes = sec(fc.circ_10,fe.intervalos[i],fe.intervalos[i+1],cond.intmax,cond.tol1,cond.tol3) 
    condicao = 1
    k = len(tuplex) 
    j = 0
    DesvioPadrão = np.std(tuplex, axis = 0, dtype = float)
    print(Solution)
    A_1 = str(round(fe.intervalos[i],3))
    A_2 = str(round(fe.intervalos[i+1],3))  
    A = str(round(Solution,3))
    B = str(round(Count,3))

    D = str(round(DesvioPadrão,3))
    a = ("[" + A_1 + "; " + A_2 + "]" + "& " + A + "& " + B + "& " + D  + "\n "  )
    file_object.write(a)
    
      # cada tabela um tipo de intervalo
  # arredondar números
  # fazer para os quadrados
    