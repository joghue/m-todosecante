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
    a = np.linspace(min(lista), max(lista), 50)
    cubic_interp = interp1d(lista,funcoes, kind='cubic') 
    resultados = cubic_interp(a)
    a = plt.plot(resultados,'r')
    img_02 = plt.plot(funcoes, 'ro')
    plt.grid()
    plt.show()
def teste_2(lista):
   c = len(lista)
   a = np.linspace(min(lista), max(lista), 50)
   cubic_interp = interp1d(lista,list(range(0,c)), kind ='cubic') 
   resultados = cubic_interp(a)
   img_01 = pl.plot(resultados,'r')
   img_02 = plt.plot(lista,'ro')
   plt.grid()
   plt.show()
   
   # plot quadrado
def plot_quad(lista,x,nom_fig):
    lado_1 = matplotlib.pyplot.hlines(0,lista[0],lista[1], color = 'r')
    lado_2 = matplotlib.pyplot.hlines(lista[1],lista[0], lista[1], color = 'r')
    lado_3 = matplotlib.pyplot.vlines(lista[0],0,lista[1] ,color ='r')
    lado_4 = matplotlib.pyplot.vlines(lista[1],0,lista[1],color ='r')
    Lado_1 = matplotlib.pyplot.hlines(0,x, lista[0], color = 'g')
    Lado_2 = matplotlib.pyplot.hlines(lista[1],x,lista[0], color = 'g')
    Lado_3 = matplotlib.pyplot.vlines(lista[0],0,lista[1] ,color ='g')
    Lado_4 = matplotlib.pyplot.vlines(x,0,lista[1],color ='g')
    ax.set_aspect('equal')  
    plt.xlim([-lista[1]*3,lista[1]*3])                 #alterando eixos
    plt.ylim(-lista[1]*3,lista[1]*3) 
    plt.grid(True)
    fig.savefig(nom_fig)
    plt.title("quadrados problemáticos")
    plt.show()
# Análise quadrados
def plot_Analisequad(lista, x, circ, d, nome_fig):
    xmin = min(lista[0] - lista[1], x - lista[1]) - 1
    xmax =max(lista[0] - lista[1], x - lista[1]) + 1
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


# erros
def plot_erro(lista_erro, nome_fig):
    n = len(lista_erro)
    int_01 = np.arange(1, n+1)
    plt.plot(int_01, lista_erro, 'bD')
    plt.grid(True)
    plt.savefig(nome_fig)
    plt.savefig(nome_fig)
    plt.show()