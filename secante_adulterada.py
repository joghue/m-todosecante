# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 01:28:50 2021

@author: joaqu
"""

import math
import numpy as np
import numpy as np
import numdifftools as nd
import random
from funcpython import sec
import condicoes as cond
from math import cos, sin, radians
from scipy.optimize import minimize, NonlinearConstraint
from sympy import Symbol
from sympy import Symbol
def funTriang(xA, lista):
    # Define as funções necessárias (função, jacobiana (gradiente), hessiana)
    def fun_obj(a, xA, lista):
        z1 = max( a[0] * xA + a[1] * lista[0], 
                a[0] * ( xA + lista[1] * cos( radians( lista[4] ) ) ) + a[1] * ( lista[0] + lista[1] * sin( radians(lista[4]) ) ), 
                a[0] * ( xA + lista[2] * cos( radians( lista[3] + lista[4] ) ) ) + a[1] * ( lista[0] + lista[2] * sin( radians( lista[3] + lista[4] ) ) ) 
                )
        z2 = min( a[0] * lista[5] + a[1] * lista[6], 
                a[0] * ( lista[5] + lista[7] * cos( radians( lista[10] ) ) ) + a[1] * ( lista[6] + lista[7] * sin( radians( lista[10] ) ) ), 
                a[0] * ( lista[5] + lista[8] * cos( radians( lista[9] + lista[10] ) ) ) + a[1] * ( lista[6] + lista[8] * sin( radians( lista[9] + lista[10] ) ) )
                )
        return ( max( 0, z1 - z2 ) ) ** 2.0

    def fun_triang(a): return fun_obj(a, xA, lista)

    def grad_triang(a): return nd.Gradient(fun_triang)(a)

    def hess_triang(a): return nd.Hessian(fun_triang)(a)

    # Define a função e a jacobiana das restrições do problema ||a||_{2}^{2} = 1.0 ==> 1 <= |a||_{2}^{2} <== 1
    def cons_f(a):
        return a[0] ** 2.0 + a[1] ** 2.0

    def cons_J(a):
        return [[2.0 * a[0], 2.0 * a[1]]]

    # Parâmetros do otimizador
    a0 = np.array([1.0, 0.0])
    nonlinear_constraint = NonlinearConstraint(cons_f, 1.0, 1.0, jac=cons_J)


    k = 0

    while True:
        # Resolve o problema de minimização
        result = minimize(fun_triang, a0, method='trust-constr', jac=grad_triang, hess=hess_triang, constraints=nonlinear_constraint)
        
        # Verifica a solução
        if ( result.success == False) or (( result.fun < 10 **(-8) ) and ( result.constr_violation != 0.0 )):
            # Não resolveu o problema, ou resolveu o problema mas violou as restrições
            a0 = np.array([random.random(), random.random()])
            k = k+1
        elif k > 10:
            # Permite que sejam realizadas até 10 tentivas
            
            return result.fun[k], False
        else:
            # Resolveu o problema sem violar as restrições
          
            return result.fun, True

def Sol_Triangle( a, b, itermax, tol, tolfunc,lista):
    
    # Cálculos iniciais
   eps =    np.finfo(float).eps  
          
   f_a, Vflag = funTriang(a, lista)
   if(Vflag == False):
    a = input("Valores inválidos, insira outro")
    f_a, Vflag = funTriang(a, lista)
   
   
   f_b, Vflag = funTriang(b, lista) 
   if(Vflag == False):
     b = input("Valores inválidos, insira outro")
     f_b, Vflag = funTriang(b, lista)
 
    
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
   if (abs(f_a) < tolfunc):
        print("Tolerância da função atingida.")
        b = a
        return b, contador, lista_x, lista_erros, lista_fx,f_b
   elif (abs(f_b) < tolfunc):
        print("Tolerância da função atingida.")
        return b, contador, lista_x, lista_erros, lista_fx,f_b
   else:
        print( contador)
        # Ciclo principal
        while (abs(f_b) > tolfunc) and (contador < itermax) and (tol * abs(b) <= ea)  :
            contador += 1
            # Tenta determinar o próximo ponto c através do método da secante. Caso não consiga, toma o ponto c como o ponto médio entre a e b
            if (abs(f_a - f_b) > eps ):
                print("Iteração: método da secante")
                c = (f_b * a - f_a * b) / (f_b - f_a)
                
            else:
                print("iteração: método da bissecção")
                c = (a + b) / 2.0
            a = b
            b = c
            f_a = f_b
            Count_2 = 0
            f_b,Vflag = funTriang(c, lista)
            if(Vflag == False):
             while(Count_2 < 10 or Vflag== False):
                c = (a + b) / 2.0
                f_b =funTriang(c, lista)
                Count_2 = Count_2 + 1
                if(Count_2 >10):
                   a= -2
                   return a, b, contador, lista_x, lista_erros, lista_fx,f_b
            else: 
                  pass
                    
            ea = abs(a - b)
            # Salva alguns valores
            lista_x.append(b)
            lista_erros.append(ea)
            lista_fx.append(f_b)    
            
        if (abs(f_b) < tolfunc):
               g = print("Tolerância da função atingida.")
               return b, contador, lista_x, lista_erros, lista_fx,f_b
        elif (ea <tol  * abs(b)):
                g=  print("Tolerância atingida.")
                return b, contador, lista_x, lista_erros, lista_fx,f_b
        elif (contador > itermax ):
                g =  print("Número máximo de iterações atingido." )
                return b, contador, lista_x, lista_erros, lista_fx,f_b
  