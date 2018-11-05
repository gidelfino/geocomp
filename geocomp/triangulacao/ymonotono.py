#!/usr/bin/env python
"""Algoritmo Triangulacao de Poligono Y-Monotono"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.segment import Segment
from geocomp.common.guiprim import *

def is_adj(ia, ib, n):
	print('Adj ', ia, ' ', ib)
	if (ia == ib + 1 or ia == ib - 1):
		return True
	if (ia == 0 and ib == n - 1):
		return True
	if (ib == 0 and ia == n - 1):
		return True
	return False

def mostra_diagonal(v, w):
    print(v.x, ' ', v.y, ' ', w.x, ' ', w.y)
    Segment(v, w).hilight()

def YMonotono (l):
	"Algoritmo Triangulacao de Poligono Y-Monotono para uma lista l de pontos"
	pol = Polygon(l)
	pol.plot()
	p = []
	n = len(l)
	for i in range(0, n):
		p.append(i)
	p.sort(key=lambda x:l[x].y, reverse=True)
	for i in range (0, len(l)):
		# print(l[p[i]].x, ' ', l[p[i]].y)
		print(p[i], ' ')
	st = [0] * (n + 1)
	sz = 0
	for i in range(0, n):
		if sz <= 1:
			st[sz] = p[i]
			sz += 1
		else:
			b = st[sz - 1]
			f = st[0]
			print('back ', b, ' front ', f)
			if (is_adj(p[i], b, n) and not is_adj(p[i], f, n)):
				while (sz > 1 and left(l[p[i]], l[st[sz - 1]], l[st[0]])):
					sz -= 1
					mostra_diagonal(l[p[i]], l[st[sz - 1]])
				st[sz] = p[i]
				sz += 1
			elif (is_adj(p[i], f, n) and not is_adj(p[i], b, n)):
				aux = b
				while (sz > 1):
					mostra_diagonal(l[p[i]], l[st[sz - 1]])
					sz -= 1
				sz -= 1
				st[sz] = aux
				sz += 1
				st[sz] = p[i]
				sz += 1
			else:
				sz -= 1
				while (sz > 2):
					sz = sz - 1
					mostra_diagonal(l[p[i]], l[st[sz - 1]])




			
