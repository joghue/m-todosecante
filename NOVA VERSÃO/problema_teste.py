# -*- coding: utf-8 -*-

from solver import sec_solver

itermax = 1000
tol = 10 ** (-8)
tolfunc = 10 ** (-8)
tipo = 1

# Problema convexo

a = 0.1
b = 0.9

quadrado = [ 
            [0.0, 0.0], [3.0, 0.0], [3.0, 3.0], 
            [0.0, 0.0], [3.0, 3.0], [0.0, 3.0] 
            ]

losango  = [
            [2.0, 0.0], [4.0, 2.0], [6.0, 0.0], 
            [4.0, 2.0], [6.0, 0.0], [8.0, 2.0]
            ]

x_sol, f_sol, contador, lista_x, lista_erros, lista_fx = sec_solver( a, b, quadrado, losango, tipo, itermax, tol, tolfunc, True )

# Problema misto

a = -1.0
b = 0.5

letra_u = [
            [1.0, -7.0], [1.0, -4.0], [2.0, -4.0],
            [1.0, -7.0], [2.0, -4.0], [2.0, -7.0],
            [2.0, -4.0], [2.0, -5.0], [5.0, -5.0],
            [2.0, -4.0], [5.0, -5.0], [5.0, -4.0],
            [5.0, -4.0], [5.0, -7.0], [6.0, -7.0],
            [5.0, -4.0], [6.0, -7.0], [6.0, -4.0]
            ]

triangulo = [
                [5.0, -7.0], [7.0, -7.0], [6.0, -5.0]
                ]

#x_sol, f_sol, contador, lista_x, lista_erros, lista_fx = sec_solver( a, b, quadrado, losango, tipo, itermax, tol, tolfunc, True )

print(x_sol)
print(f_sol)