# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:06:27 2020

@author: joaqu
"""
import math
def sec(fun, a, b, itermax, tol, tolfunc):
    # Cálculos iniciais                
    f_a = fun(a)
    f_b = fun(b)
    ea = abs(a - b)
    contador = 0
    # Cria listas vazias
    lista_x = []
    lista_fx = []
    lista_erros = []
    # Salva alguns valores
    lista_x.append(a)
    lista_x.append(b)
    lista_fx.append(f_a)
    lista_fx.append(f_b)
    lista_erros.append(ea)
    # Verifica se f(a) ou f(b) é menor que a tolerância, caso contrário entra no ciclo principal
    if (f_a < tolfunc):
        print("Tolerância da função atingida.")
        b = a
    elif (f_b < tolfunc):
        print("Tolerância da função atingida.")
    else:
        # Ciclo principal
        while (contador < itermax) and (tol * abs(b) <= ea) and (abs(f_b) > tolfunc):
            contador += 1
            # Tenta determinar o próximo ponto c através do método da secante. Caso não consiga, toma o ponto c como o ponto médio entre a e b
            try:
                c = (f_b * a - f_a * b) / (f_b - f_a)
            except (ZeroDivisionError):
                c = (a + b) / 2.0
            a = b
            b = c
            f_a = f_b
            f_b = fun(c)
            ea = abs(a - b)
            # Salva alguns valores
            lista_x.append(b)
            lista_erros.append(ea)
            lista_fx.append(f_b)
        else:
            if (contador > itermax):
                print("Número máximo de iterações atingido.")
            if (tol * abs(b) < ea):
                print("Tolerância atingida.")
            if (abs(f_b) < tolfunc):
                print("Tolerância da função atingida.")
    return b, contador, lista_x, lista_erros, lista_fx