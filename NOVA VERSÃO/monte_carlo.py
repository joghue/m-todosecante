# -*- coding: utf-8 -*-

from numpy.random import seed

__NUMERO_PRIMO_GRANDE__ = 1001311

seed(__NUMERO_PRIMO_GRANDE__)

def estima_intersecao(l, u, n1, c1, n2, c2, NUM_POINTS=10000):
    """Recebe os vertices inferiores (l) e superiores (u) de um retangulo
    que contem a possivel intersecao entre os objetos, as normais (n1
    e n2) e constantes (c1 e c2) que definem os semiplanos associados
    com os objetos convexos (triangulo, mas pode ser outra coisa) e
    devolve uma estimativa para a area de intersecao entre os objetos.

    """

    from numpy.random import uniform
    from numpy import dot, prod, subtract
    
    count = 0

    for i in range(NUM_POINTS):

        p = uniform(l, u)

        stop = False

        # Verifica se esta dentro do obj1
        for n, c in zip(n1, c1):

            if dot(n, p) > c:

                stop = True
                break

        if stop: continue

        # Verifica se esta dentro do obj2
        for n, c in zip(n2, c2):
            
            if dot(n, p) > c:

                stop = True
                break

        # Se esta dentro dos dois, incrementa o contador
        if not stop: count += 1

    # Estimativa da area de intersecao
    return (count / NUM_POINTS) * prod(subtract(u, l))

def calcula_normais_e_c(v):

    from numpy import dot, array
    
    nv = len(v)

    n = [array([t[1], -t[0]]) for t in ((v[(i + 1) % nv] - v[i]) for i in range(nv))]

    c = [dot(n[i], v[i]) for i in range(nv)]
    
    for i in range(nv):

        if dot(n[i], v[(i + 2) % nv]) > c[i]:
            n[i] *= -1.0
            c[i] *= -1.0

    return n, c