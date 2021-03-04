# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:45:20 2020

@author: joaqu
"""
import math
import listas as lt
def fs(lista):   
      return lambda x: (lista[0]-x)**2 +  (lista[1] - lista[2])**2 - (lista[3] + lista[4])**2
def fsqrt(lista): 
   return lambda x:math.sqrt((lista[0]-x)**2 +  (lista[1] - lista[2])**2) - (lista[3] + lista[4])
circ_1 = fs(lt.lista_1)
circ_2 = fsqrt(lt.lista_2)
circ_3 = fsqrt(lt.lista_3)
circ_4 = fsqrt(lt.lista_4)
circ_5 = fsqrt(lt.lista_5)
circ_6 = fsqrt(lt.lista_6)
circ_7 = fsqrt(lt.lista_7)
circ_8 = fsqrt(lt.lista_8)
circ_9 = fsqrt(lt.lista_9)
circ_10 = fsqrt(lt.lista_10)
