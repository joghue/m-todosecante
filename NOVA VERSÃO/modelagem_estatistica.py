# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Simulacao para o cálculo da sobreposição usando Monte Carlo 

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

def fun_simulacao(x, obj_fixo, obj_movel, verbose):

    from numpy import array
    from monte_carlo import estima_intersecao, calcula_normais_e_c


    # Calcula o número de triângulos que compõe cada objeto
    n = len(obj_fixo) // 3
    m = len(obj_movel) // 3

    # Inicializa arrays e variáveis
    resultado = 0.0
    nm = n * m
    l = 1

    for j in range(m):
        
        # Calcula as normais e os deslocamentos para os triângulos que compõem o objeto movel deslocado
        obj_movel_j = [
                        array([x + obj_movel[3 * j][0], obj_movel[3 * j][1]]), 
                        array([x + obj_movel[3 * j + 1][0], obj_movel[3 * j + 1][1]]), 
                        array([x + obj_movel[3 * j + 2][0], obj_movel[3 * j + 2][1]])
                        ]
        n_movel, c_movel = calcula_normais_e_c(obj_movel_j)
        
        for i in range(n):

            # Calcula as normais e os deslocamentos para os triângulos que compõem o objeto fixo
            obj_fixo_i = [ 
                            array(obj_fixo[3 * i]), 
                            array(obj_fixo[3 * i + 1]), 
                            array(obj_fixo[3 * i + 2]) 
                            ]
            n_fixo, c_fixo = calcula_normais_e_c(obj_fixo_i)

            # Calcula os extremos da caixa que contém os objetos.
            min_x = min( obj_movel_j[0][0], obj_movel_j[1][0], obj_movel_j[2][0], obj_fixo_i[0][0], obj_fixo_i[1][0], obj_fixo_i[2][0] )
            max_x = max( obj_movel_j[0][0], obj_movel_j[1][0], obj_movel_j[2][0], obj_fixo_i[0][0], obj_fixo_i[1][0], obj_fixo_i[2][0] )
            min_y = min( obj_movel_j[0][1], obj_movel_j[1][1], obj_movel_j[2][1], obj_fixo_i[0][1], obj_fixo_i[1][1], obj_fixo_i[2][1] )
            max_y = max( obj_movel_j[0][1], obj_movel_j[1][1], obj_movel_j[2][1], obj_fixo_i[0][1], obj_fixo_i[1][1], obj_fixo_i[2][1] )

            # Estima a interseção entre os objetos.
            intersecao_ij = estima_intersecao([min_x, min_y], [max_x, max_y], n_movel, c_movel, n_fixo, c_fixo)

            # Imprime informação.
            if verbose == True:

                print("---> Resolvendo: ", l, " de ", nm, " ...")

            # Atualiza o contador.
            l = l + 1

            # Soma o resultado parcial ao valor acumulado.
            resultado = resultado + intersecao_ij

    return resultado / nm, True
