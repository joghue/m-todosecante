# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:55:23 2020

@author: joaqu
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib 
import math
from scipy.interpolate import interp1d
import pylab as pl
fig, ax = plt.subplots()
#encontro das duas cicunferências
def plot_solucao(lista, x, nome_fig):
    circulo = plt.Circle((lista[0], lista[1]), lista[3], color='red', fill=False)
    circulo1 = plt.Circle((x, lista[2]), lista[4], color='blue', fill=False)
    xmin = min(lista[0] - lista[3], x - lista[4]) - 1
    xmax = max(lista[0] + lista[3], x +lista[4]) + 1
    ymin = min(lista[1] - lista[3], lista[2] - lista[4]) - 1
    ymax = max(lista[1] + lista[3], lista[2] + lista[4]) + 1
    ax.set_xlim((xmin, xmax))
    ax.set_ylim((ymin, ymax))
    ax.set_aspect('equal')
    ax.add_artist(circulo)
    ax.add_artist(circulo1)
    plt.grid(True)
    plt.title("solução das circunferências")
    fig.savefig(nome_fig)
    plt.show()
    #análise circunferências
def plot_analise(lista, x, circ, d, nome_fig):
    xmin = min(lista[0] - lista[3], x - lista[4]) - 1
    xmax = max(lista[0] + lista[3], x + lista[4]) + 1
    int_01 = np.arange(xmin, xmax, 0.01)
    img_01 = np.array([circ(x) for x in int_01])
    img_02 = np.array([circ(x) for x in d])
    n = len(d)
    texto = np.arange(1, n)
    for i, txt in enumerate(texto):
        plt.annotate(txt, (d[i], img_02[i]))
    plt.grid(True)
    plt.plot(int_01, img_01, 'g--', d, img_02, 'bs')
    plt.show()

def teste(lista,funcoes):
    a = np.linspace(min(lista), max(lista), 40)
    cubic_interp = interp1d(lista,funcoes, kind='cubic') 
    resultados = cubic_interp(a)
    a = plt.plot(resultados,'r')
    img_02 = plt.plot(funcoes, 'ro')
    plt.grid()
    plt.show()
def teste_2(lista):
   c = len(lista)
   a = np.linspace(min(lista), max(lista), 40)
   cubic_interp = interp1d(lista,list(range(0,c)), kind ='cubic') 
   resultados = cubic_interp(a)
   img_01 = pl.plot(resultados,'r')
   img_02 = plt.plot(lista,'ro')
   plt.grid()
   plt.show()
   
   # plot quadrado
def plot_quad(lista, x, nome_fig):
    #Subplots
    fig1, ax1 = plt.subplots()
    #Título do gráfico
    ax1.set_title("plot da solução dos quadrados")
    #Plot do quadrado fixo (vermelho)
    plt.hlines(0, lista[0], lista[0] + lista[1], color = 'r')
    plt.hlines(lista[1], lista[0], lista[0] + lista[1], color = 'r')
    plt.vlines(lista[0], 0, lista[1], color = 'r')
    plt.vlines(lista[0] + lista[1], 0, lista[1], color = 'r')
    #Plot do quadrado da solução (azul)
    plt.hlines(0, x, x + lista[1], color = 'b')
    plt.hlines(lista[1], x, x + lista[1], color = 'b')
    plt.vlines(x, 0, lista[1], color = 'b')
    plt.vlines(x + lista[1], 0, lista[1], color = 'b')
    #Eixos
    a = min(lista[0], x)
    b = max(lista[0], x) + lista[1]
    c = max(0.1 * abs(a), 0.1 * abs(b), 1)
    l_a = a - c
    l_b = b + c
    r = abs(l_b - l_a)
    plt.xlim(l_a, l_b)
    plt.ylim(- r/2, r/2) 
    #Aspecto do gráfico
    ax1.set_aspect('equal')
    plt.grid()
    fig1.savefig(nome_fig)
    plt.show()

def triplot(solucao,lista,lista_movel):
    for j in range(len(lista_movel)):
       lista_movel[j][0] = lista_movel[j][0] + solucao
    size = len(lista_movel)
    i = 0
    Size = len(lista)
    k = 0
    while(k<Size): 
     plt.plot([lista[k][0],lista[k+1][0],lista[k+2][0],lista[k][0]], [lista[k][1],lista[k+1][1],lista[k+2][1],lista[k][1]])
     k = k +3
    while(i<size): 
     plt.plot([lista_movel[i][0],lista_movel[i+1][0],lista_movel[i+2][0],lista_movel[i][0]], [lista_movel[i][1],lista_movel[i+1][1],lista_movel[i+2][1],lista_movel[i][1]])
     i = i +3
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    fig = plt.plot()


   
     # lim inf x- min(lista[o],x)- 0.1*min(lista[o],x),max(lista[1]+lista[0], lista[1]+x)
     # min(lista[1])
# Análise quadrados
def plot_Analisequad(lista, x, circ, d, nome_fig):
    plt.title("plot de pontos por iteração")
    xmin = min(lista[0] - lista[1], x + lista[1]) - 1
    xmax =max(lista[0] - lista[1], x + lista[1]) + 1
    int_01 = np.arange(xmin, xmax, 0.001)
    img_01 = np.array([circ(x) for x in int_01])
    img_02 = np.array([circ(x) for x in d])
    n = len(d)
    texto = np.arange(1, n)
    for i, txt in enumerate(texto):
        plt.annotate(txt, (d[i], img_02[i]))
    plt.grid(True)
    plt.plot(int_01, img_01, 'g--', d, img_02, 'bs')
    plt.show()

def Analise_tri(F_x, x):
    plt.grid(True)
    plt.plot(F_x,x,'o')
# erros
def plot_erro(lista_erro, nome_fig):
    n = len(lista_erro)
    int_01 = np.arange(1, n+1)
    plt.plot(int_01, lista_erro, 'bD')
    plt.grid(True)
    plt.savefig(nome_fig)
    plt.savefig(nome_fig)
    plt.show()