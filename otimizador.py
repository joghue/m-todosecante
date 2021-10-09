# -*- coding: utf-8 -*-

import numpy as np

from scipy.optimize import minimize

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Define a função e a jacobiana das restrições do problema ||a||_{2}^{2} = 1.0 <==> 1 <= ||a||_{2}^{2} <= 1.

def fun_restricoes(a): return a[0] ** 2.0 + a[1] ** 2.0

def jac_restricoes(a): return [[2.0 * a[0], 2.0 * a[1]]]

# Define a função do otimizador.

def fun_otimizador(a0, funcao, gradiente, hessiana, restricoes):

    eps = np.finfo(float).eps

    k = 0
    while True:
        
        # Resolve o problema de otimização.
        
        resultado = minimize( funcao, a0, method='trust-constr', jac = gradiente, hess = hessiana, constraints = restricoes,options={'verbose':3,'gtol':1e-4})

        # Verifica a solução.

        if ( resultado.success == False  and ( resultado.constr_violation >= 0.9 )):
            print("dentro")
            # Não resolveu o problema, ou resolveu o problema violando as restrições.

            a0 = np.random.rand(2)
            k = k + 1

        elif k > 10:

            # Permite que sejam realizadas até 10 tentivas para a solução do problema de otimização. Caso não consiga resolver, retorna o valor booleano 'False'.
            
            return resultado.fun, False

        else:

            # Resolveu o problema sem violar as restrições.
          
            return resultado.fun, True