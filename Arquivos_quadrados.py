# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:25:38 2020

@author: joaqu
"""
"""arquivo para experimentação e modelagem"""
def quadrado(lista):
    return lambda x:max(0,abs(x+lista[1]-lista[0]))*max(0,abs(lista[0]+lista[1]-x))


import condicoes as cond
import grafico as gr
from funcpython import sec 
import feradores as fe
import numpy as np

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

i = 0
j = 0
file_name = "resultado.quadrado.tex"
with open(file_name,"w") as file_object:
 for i in range(0,4):
    str(i)
    Solution,Count,tuplex,error,funcoes = sec(quadrado(lista_0),fe.intervalos[i],fe.intervalos[i+1],cond.intmax,cond.tol1,cond.tol3) 
    
    DesvioPadrão = np.std(tuplex, axis = 0, dtype = float)
    print(Solution)
    A_1 = str(round(fe.intervalos[i],3))
    A_2 = str(round(fe.intervalos[i+1],3))  
    A = str(round(Solution,3))
    B = str(round(Count,3))

    D = str(round(DesvioPadrão,3))
    a = ("[" + A_1 + "; " + A_2 + "]" + "& " + A + "& " + B + "& " + D  + "\n "  )
    file_object.write(a)

gr.plot_quad(lista_3,Solution,"fig")
gr.plot_Analisequad(lista_3,Solution,quadrado(lista_3),tuplex,"fig2")
gr.plot_erro(error,"fig4")
print(Solution)
print(tuplex)
print(Count)
print(error)
       