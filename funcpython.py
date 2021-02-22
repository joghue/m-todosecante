# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:06:27 2020

@author: joaqu
"""
import math
def sec(fun, x,b,tol,IterMax,tolfunc):                    
    f_a = fun(x)
    f_b = fun(b)
    EA = abs(x-b)
    Contador = 0     
    listax=  []
    erros = []
    listax.append(x)
    listax.append(b)
    erros.append(EA)
    funcoes = [f_a,f_b]
    while Contador < IterMax and tol*abs(b)<=EA and abs(f_a)>tolfunc:
        try:
           Contador += 1 
           x_1 = (f_b*x - f_a*b)/(f_b- f_a)
           x = b
           b = x_1
           f_a = f_b
           f_b = fun(b)
           EA = abs(x-b)        
           listax.append(x_1)
           erros.append(EA)
           funcoes.append(f_a)
        except(ZeroDivisionError):
            x_1 = (x + b)/2
    else:
            if(Contador>IterMax):
                print("Número de iterações ultrapassdas")
            if(tol*abs(b)>EA):
                print("tolerância atingida")
            if(abs(f_a)<tolfunc):
                print("tolerância da função")
    return x_1,Contador,listax,erros,funcoes
    