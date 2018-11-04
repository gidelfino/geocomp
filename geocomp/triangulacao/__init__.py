# -*- coding: utf-8 -*-

"""Algoritmo para o problema de triangulação de polígonos:
 Dado um conjunto de pontos, determinar uma triangulacao do poligono formado por esses pontos.

 Algoritmos disponiveis:
- Y monotono
- Lee e Preparata
- Triangulacao por remoção de orelhas
 
algoritmo otimo = executa em tempo O(n lg(n)), n = numero de pontos,
"""
from . import ymonotono
from . import orelha

# cada entrada deve ter:
#  [ 'nome-do-modulo', 'nome-da-funcao', 'nome do algoritmo' ]
children = [
	['ymonotono', 'YMonotono', 'Y-Monotono' ],
	['orelha', 'Orelha', 'Remoção de orelhas' ]
]

__all__ = [a[0] for a in children]
