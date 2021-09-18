# -*- coding: utf-8 -*-

import numpy as np
import math

from modelagem_caso_convexo import fun_conv
from modelagem_caso_concavo import fun_conc
from modelagem_caso_misto import fun_misto

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Formato:

# a :: real
# b :: real
# obj_fixo  :: [[A^1_1(x), A^1_1(y)], [A^1_2(x), A^1_2(y)], [A^1_3(x), A^1_3(y)], ..., [A^n_1(x), A^n_1(y)], [A^n_2(x), A^n_2(y)], [A^n_3(x), A^n_3(y)]]
# obj_movel :: [[B^1_1(x), B^1_1(y)], [B^1_2(x), B^1_2(y)], [B^1_3(x), B^1_3(y)], ..., [B^n_1(x), B^n_1(y)], [B^n_2(x), B^n_2(y)], [B^n_3(x), B^n_3(y)]]
# tipo_problema :: inteiro
#       0 --> os dois objetos são convexos
#       1 --> ao menos um dos objetos é convexo
#       2 --> os dois objetos são côncavos (ou não há garantia de que são convexos)
# itermax :: inteiro
# tol :: real
# tolfunc :: real
# verbose :: bool


def sec_solver( a, b, obj_fixo, obj_movel, tipo_problema, itermax, tol, tolfunc, verbose ):

    # Define a função objetivo com base no tipo de problema.

    if tipo_problema == 0:

        def fun_obj(x): return fun_conv(x, obj_fixo, obj_movel)

    elif tipo_problema == 1:

        def fun_obj(x): return fun_misto(x, obj_fixo, obj_movel, verbose)

    elif tipo_problema == 2:

        def fun_obj(x): return fun_conc(x, obj_fixo, obj_movel, verbose)

    else:

        print("'tipo_problema': o valor informado é inválido.\n")
        print("O valores possíveis são: \n")
        print("0 --> objetos convexos. \n")
        print("1 --> objetos mistos. \n")
        print("2 --> objetos côncavos. \n")

        return math.inf, math.inf, 0, [], [], []
    
    # Verificação inicial

    if verbose == True:

        print("Verificando o valor de função em 'a'.")
    
    f_a, Vflag = fun_obj(a)
    if ( Vflag == False ):

        print("Erro: Tente outro valor para 'a'.")
        return math.inf, math.inf, 0, [], [], []
   
    if verbose == True:

        print("Verificando o valor de função em 'b'.")

    f_b, Vflag = fun_obj(b)
    if ( Vflag == False ):
        
        print("Erro: Tente outro valor para 'a'.")
        return math.inf, math.inf, 0, [], [], []

    # Cria algumas constantes e variáveis.
    eps = np.finfo(float).eps
    ea = abs(a - b)
    contador = 0

    # Cria listas vazias.
    lista_x = []
    lista_fx = []
    lista_erros = []

    # Salva alguns valores.
    lista_x.append(a)
    lista_x.append(b)
    lista_fx.append(f_a)
    lista_fx.append(f_b)
    lista_erros.append(ea)

    # Verifica se f(a) ou f(b) é menor que a tolerância, caso contrário entra no ciclo principal.
    if ( abs(f_a) < tolfunc ):

        print("Tolerância da função atingida.")
        return a, f_a, contador, lista_x, lista_erros, lista_fx

    elif ( abs(f_b) < tolfunc ):
        
        print("Tolerância da função atingida.")
        return b, f_b, contador, lista_x, lista_erros, lista_fx


    # Ciclo principal
    while ( abs(f_b) > tolfunc ) and ( contador < itermax ) and ( tol * abs(b) <= ea ):

        # Tenta determinar o próximo ponto 'c' através do método da secante. Caso não consiga, toma o ponto 'c' como o ponto médio entre 'a' e 'b'.
        if ( abs( f_a - f_b ) > eps ):

            if verbose == True:

                print("\nIteração ", contador, ": Método da Secante.")
            
            c = (f_b * a - f_a * b) / (f_b - f_a)
                
        else:

            if verbose == True:

                print("\nIteração ", contador, ": Ponto Médio.")
            
            c = (a + b) / 2.0

        a = b
        b = c
        f_a = f_b
        f_b, Vflag = fun_obj(c)
        contador_2 = 0

        if ( Vflag == False ):

            while ( contador_2 < 10 or Vflag == False ):

                if verbose == True:

                    print("--> Tentativa: ", contador_2)

                c = (a + b) / 2.0
                f_b, Vflag = fun_obj(c)
                contador_2 = contador_2 + 1
                b = c

                if ( contador_2 > 10 ):

                    print("Erro: O método excedeu o número de tentativas para um novo passo.")
                    return  b, f_b, contador, lista_x, lista_erros, lista_fx

        ea = abs(a - b)

        # Salva alguns valores
        lista_x.append(b)
        lista_erros.append(ea)
        lista_fx.append(f_b)    
            
        if ( abs(f_b) < tolfunc ):

            print("Tolerância da função atingida.")
            return b, f_b, contador, lista_x, lista_erros, lista_fx

        elif ( ea < tol * abs(b) ):

            print("Tolerância atingida.")
            return b, f_b, contador, lista_x, lista_erros, lista_fx

        elif ( contador > itermax ):

            print("Número máximo de iterações atingido.")
            return b, f_b, contador, lista_x, lista_erros, lista_fx
        
        contador += 1