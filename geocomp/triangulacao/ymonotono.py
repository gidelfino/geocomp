#!/usr/bin/env python
"""Algoritmo Triangulacao de Poligono Y-Monotono"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.segment import Segment
from geocomp.common.guiprim import *
from functools import *
from math import *

def is_adj(ia, ib, n):
    if (ia == ib + 1 or ia == ib - 1):
        return True
    if (ia == 0 and ib == n - 1):
        return True
    if (ib == 0 and ia == n - 1):
        return True
    return False

def mostra_diagonal(v, w):
    Segment(v, w).hilight()
    control.sleep()

def YMonotono (l, print_polygon = True):
    "Algoritmo Triangulacao de Poligono Y-Monotono para uma lista l de pontos"
    if print_polygon:
        pol = Polygon(l)
        pol.plot()
    n = len(l)
    p = [i for i in range(n)]

    def compare(a, b):
        if (l[a].y != l[b].y):
            return l[b].y - l[a].y
        return l[a].x - l[b].x
    p.sort(key=cmp_to_key(compare))

    poly_on_left = (p[1] + 1) % n == p[0]
    
    st = [0] * (n + 1)
    sz = 0
    for i in range(0, n):
        if sz <= 1:
            st[sz] = p[i]
            sz += 1
        else:
            b = st[sz - 1]
            f = st[0]
            if (is_adj(p[i], b, n) and not is_adj(p[i], f, n)):
                print('Case 1')
                while (sz > 1):
                    b = st[sz - 1]
                    c = st[sz - 2]
                    if poly_on_left:
                        b, c = c, b
                    if (left(l[c], l[b], l[p[i]])): # angulo < 180
                        sz -= 1
                        mostra_diagonal(l[p[i]], l[st[sz - 1]])
                    else:
                        break
                st[sz] = p[i]
                sz += 1
            elif (is_adj(p[i], f, n) and not is_adj(p[i], b, n)):
                print('Case 2')
                poly_on_left = not poly_on_left
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
                print('Case 3')
                while (sz > 2):
                    sz = sz - 1
                    mostra_diagonal(l[p[i]], l[st[sz - 1]])



            
