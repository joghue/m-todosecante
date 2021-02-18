# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:55:23 2020

@author: joaqu
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib 
import math
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
 
   # plot quadrado
def plot_quad(lista,x,nom_fig):
    Ponto = lista[1]/2
    Quadrado = matplotlib.patches.Rectangle((lista[0]+Ponto,Ponto),lista[1],lista[1], fc ='none', ec ='r', lw = 2) 
    quadrado = matplotlib.patches.Rectangle((x+Ponto,Ponto),lista[1],lista[1], fc ='none', ec ='g', lw = 2) 
    ax.set_aspect('equal')
    ax.add_patch(Quadrado)
    ax.add_patch(quadrado)
    plt.xlim([-lista[1]*3,lista[1]*3])                 #alterando eixos
    plt.ylim(-lista[1]*3,lista[1]*3) 
    plt.grid(True)
    fig.savefig(nom_fig)
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