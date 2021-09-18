# -*- coding: utf-8 -*-

import numpy as np
import numdifftools as nd

from scipy.optimize import minimize, NonlinearConstraint
from otimizador import fun_otimizador, fun_restricoes, jac_restricoes

# Formato:
# x = número real
# obj_fixo  = [[A^1_1(x), A^1_1(y)], [A^1_2(x), A^1_2(y)], [A^1_3(x), A^1_3(y)], ..., [A^n_1(x), A^n_1(y)], [A^n_2(x), A^n_2(y)], [A^n_3(x), A^n_3(y)]]
# obj_movel = [[B^1_1(x), B^1_1(y)], [B^1_2(x), B^1_2(y)], [B^1_3(x), B^1_3(y)], ..., [B^n_1(x), B^n_1(y)], [B^n_2(x), B^n_2(y)], [B^n_3(x), B^n_3(y)]]

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Modelagem para o caso 'côncavo-côncavo'.

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Define a função interna do problema.

def fun_interna_conc(a, idx_fixo, idx_movel, x, obj_fixo, obj_movel):

    v = max( np.dot(a, obj_fixo[3 * idx_fixo]), np.dot(a, obj_fixo[3 * idx_fixo + 1]), np.dot(a, obj_fixo[3 * idx_fixo + 2]) )

    w = min(
            a[0] * ( x + obj_movel[3 * idx_movel][0] ) + a[1] * obj_movel[3 * idx_movel][1],  
            a[0] * ( x + obj_movel[3 * idx_movel + 1][0] ) + a[1] * obj_movel[3 * idx_movel + 1][1],
            a[0] * ( x + obj_movel[3 * idx_movel + 2][0] ) + a[1] * obj_movel[3 * idx_movel + 2][1],
            )

    return ( max(0.0, v - w) ) ** 2.0


# Define a função principal.

def fun_conc(x, obj_fixo, obj_movel, verbose):

    # Define os parâmetros do otimizador.

    a_inicial = np.array([1.0, 0.0])
    restricao = NonlinearConstraint(fun_restricoes, 1.0, 1.0, jac = jac_restricoes)

    n = len(obj_fixo) // 3
    m = len(obj_movel) // 3

    resultado = 0.0
    l = 1

    for i in range(n):

        for j in range(m):

            # Define a função objetivo, o gradiente e a hessiana, para aquela iteração.

            def fun_objetivo(a): return fun_interna_conc(a, i, j, x, obj_fixo, obj_movel)

            def grad_objetivo(a): return nd.Gradient(fun_objetivo)(a)

            def hess_objetivo(a): return nd.Hessian(fun_objetivo)(a)

            # Chama o otimizador e resolve a instância (i, j) do problema

            valor, confiavel = fun_otimizador(a_inicial, fun_objetivo, grad_objetivo, hess_objetivo, restricao)

            if verbose == True:

                print("---> Resolvendo: ", l, " de ", n * m, " ...")

            l = l + 1

            if confiavel == True:

                resultado = resultado + valor

            else:

                return 0.0, False
    
    return resultado, True



                

        

