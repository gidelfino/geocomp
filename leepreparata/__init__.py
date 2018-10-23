# -*- coding: utf-8 -*-

"""Algoritmo para o problema de triangulação de polígonos:

Dado um conjunto de pontos, determinar uma triangulacao do poligono formado por esses pontos.

Algoritmos disponiveis:
- Lee e Preparata
- Triangulacao por orelhas

algoritmo otimo = executa em tempo O(n lg(n)), n = numero de pontos,                                               
"""
from . import ymonotono

children = [
	['ymonotono', 'YMonotono', 'Y-Monotono' ]
]

__all__ = [a[0] for a in children]
