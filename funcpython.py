# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:06:27 2020

@author: joaqu
"""
import math
def sec(fun, x,h,tol,IterMax,tolfunc):                    
    f_a = fun(x)
    f = fun(h)
    EA = abs(x-h)
    Contador = 0     
    listax=  []
    erros = []
    listax.append(x)
    listax.append(h)
    erros.append(EA)
    while Contador < IterMax and tol*abs(h)<=EA and abs(f_a)>tolfunc:
        try:
           Contador += 1 
           x_1 = (f*x - f_a*h)/(f_a- f)
           x = h
           h = x_1
           f_a = f
           f = fun(h)
           EA = abs(x-h)        
           listax.append(x_1)
           erros.append(EA)               
        except(ZeroDivisionError):
            x_1 = (x + h)/2
    else:
            if(Contador>IterMax):
                print("Número de iterações ultrapassdas")
            if(tol*abs(h)>EA):
                print("tolerância atingida")
            if(abs(f_a)<tolfunc):
                print("tolerância da função")
    return x_1,Contador,listax,erros
    