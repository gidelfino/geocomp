#!/usr/bin/env python
"""Algoritmo Triangulacao de Poligono Y-Monotono"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.guiprim import *

def compare(p1, p2):
	return p1.y < p2.y

def YMonotono (l):
	"Algoritmo Triangulacao de Poligono Y-Monotono para uma lista l de pontos"
	p = [0, 2, 1, 3]
	st = [0] * (len(l) + 1)
	sz = 0
	for i in range (0, len(p)):
		if len(st) == 0:
			st.append(p[i])
			sz = sz + 1
		else:
			lst = st[sz - 1]
			#vizinho da base da pilha
			if ((lst > 0 and l[lst - 1] == l[p[i]]) or (lst < len(l) - 1 and l[lst + 1] == l[p[i]])):
				while(sz > 1 and left(l[p[i]], l[p[sz - 2]], l[p[sz - 1]])):
					sz = sz - 1
					print('Diagonal ', l[p[i]].__repr__(), ' ', l[p[sz]].__repr__())
				st[sz] = p[i]
				sz = sz + 1
			else:
				while (sz > 1):
					sz = sz - 1
					print('Diagonal ', l[p[i]].__repr__(), ' ', l[p[sz]].__repr__())
				sz = sz - 1
				st[sz] = lst
				sz = sz + 1
				st[sz] = p[i]
				sz = sz + 1

	tr = Polygon (l)
	return tr
