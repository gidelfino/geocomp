# -*- coding: utf-8 -*-
"""Algoritmos para o problema do Par Mais Distante:

Dado um conjunto de pontos S, determinar dois cuja distancia entre eles 
maxima

Algoritmos disponveis:
- Forca bruta
"""
from . import brute

children = [
	[ 'brute', 'Brute', 'Forca Bruta' ]
]

__all__ = [a[0] for a in children]
