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
# função 
Solution,Count,tuplex,error,funcoes = sec(fc.circ_9,cond.initial,cond.second,cond.tol1,cond.intmax,cond.tol3) 
condicao = 1
print(Solution)
print(Count)

k = len(tuplex) 
print (k)
i = 0
j = 0

DesvioPadrão = np.std(tuplex, axis = 0, dtype = float)
print(DesvioPadrão)
print(tuplex)
# gráficos
if (condicao == 1):
    plot_solucao(lt.lista_5,Solution,"soluc1")
    plot_analise(lt.lista_5,Solution, fc.circ_5,tuplex,"fig3")
    plot_erro(error,"fig2")
    teste(tuplex,funcoes)
    teste_2(tuplex)
