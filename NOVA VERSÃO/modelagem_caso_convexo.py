# -*- coding: utf-8 -*-

import numpy as np
import numdifftools as nd

from scipy.optimize import minimize, NonlinearConstraint
from otimizador import fun_otimizador, fun_restricoes, jac_restricoes

# Formato:
# x = número real
# obj_fixo  = [[A^1_1(x), A^1_1(y)], [A^1_2(x), A^1_2(y)], [A^1_3(x), A^1_3(y)], ..., [A^n_1(x), A^n_1(y)], [A^n_2(x), A^n_2(y)], [A^n_3(x), A^n_3(y)]]
# obj_movel = [[B^1_1(x), B^1_1(y)], [B^1_2(x), B^1_2(y)], [B^1_3(x), B^1_3(y)], ..., [B^m_1(x), B^m_1(y)], [B^m_2(x), B^m_2(y)], [B^m_3(x), B^m_3(y)]]

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Modelagem para o caso 'convexo-convexo'.

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Define a função interna do problema.

def fun_interna_conv(a, x, obj_fixo, obj_movel):

    n = len(obj_fixo) // 3
    m = len(obj_movel) // 3

    sol = 0.0
    for i in range(n):

        v = max( np.dot(a, obj_fixo[3 * i]), np.dot(a, obj_fixo[3 * i + 1]), np.dot(a, obj_fixo[3 * i + 2]) )

        for j in range(m):

            w = min( 
                    a[0] * ( x + obj_movel[3 * j][0] ) + a[1] * obj_movel[3 * j][1],  
                    a[0] * ( x + obj_movel[3 * j + 1][0] ) + a[1] * obj_movel[3 * j + 1][1],
                    a[0] * ( x + obj_movel[3 * j + 2][0] ) + a[1] * obj_movel[3 * j + 2][1],
                    )

            #sol = sol + ( max( 0.0, v - w ) ) ** 2.0
            sol = max( 0.0, v - w, sol )
        
    return sol

# Define a função principal.

def fun_conv(x, obj_fixo, obj_movel):

    # Define a função objetivo, o gradiente e a hessiana.

    def fun_objetivo(a): return fun_interna_conv(a, x, obj_fixo, obj_movel)

    def grad_objetivo(a): return nd.Gradient(fun_objetivo)(a)

    #def hess_objetivo(a): return nd.Hessian(fun_objetivo)(a)

    def hess_objetivo(a): return np.zeros((2, 2))
    
    # Define os parâmetros do otimizador.

    a_inicial = np.array([1.0, 0.0])

    restricao = NonlinearConstraint(fun_restricoes, 1.0, 1.0, jac = jac_restricoes)

    return fun_otimizador(a_inicial, fun_objetivo, grad_objetivo, hess_objetivo, restricao)

