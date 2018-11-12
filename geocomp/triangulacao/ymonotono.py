#!/usr/bin/env python
"""Algoritmo Triangulacao de Poligono Y-Monotono"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.segment import Segment
from geocomp.common.guiprim import *
from functools import *
from math import *

def is_adj(ia, ib, n):
    # print('Adj ', ia, ' ', ib)
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


def test_angle(a, b, c):
    dab = sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y))
    dbc = sqrt((b.x - c.x) * (b.x - c.x) + (b.y - c.y) * (b.y - c.y))
    dac = sqrt((a.x - c.x) * (a.x - c.x) + (a.y - c.y) * (a.y - c.y))
    angle = acos((dab * dab + dbc * dbc - dac * dac)/(2 * dab * dbc))
    if (angle < 3.14159265359):
        return True
    return False

def update_next(next, l, new, old):
    nn = l[new]
    no = l[old]
    if (no.x <= nn.x):
        next[new] = old
    else:
        next[old] = new

def YMonotono (l):
    "Algoritmo Triangulacao de Poligono Y-Monotono para uma lista l de pontos"
    pol = Polygon(l)
    pol.plot()
    p = []
    n = len(l)
    temp_next = []
    for i in range(0, n):
        p.append(i)
        temp_next.append((i + 1) % n)
        

    def compare(a, b):
        if (l[a].y == l[b].y):
            return l[b].x - l[a].x
        return l[a].y - l[b].y
    p.sort(key=cmp_to_key(compare), reverse=True)
    
    for i in range (0, len(l)):
        # print(l[p[i]].x, ' ', l[p[i]].y)
        print(p[i], ' ')
    st = [0] * (n + 1)
    sz = 0
    for i in range(0, n):
        print('=================Ponto ', p[i], ' ===============================')
        if sz <= 1:
            st[sz] = p[i]
            sz += 1
        else:
            b = st[sz - 1]
            f = st[0]
            print('back ', b, ' front ', f)
            if (is_adj(p[i], b, n) and not is_adj(p[i], f, n)):
                print('Case 1')
                # while (sz > 1 and test_angle(l[p[i]], l[st[sz - 1]], l[st[sz - 2]])):
                while (sz > 1):
                    b = st[sz - 1]
                    c = st[sz - 2]
                    if (temp_next[c] != b):
                        temp = c
                        c = b
                        b = temp
                    if (left(l[c], l[b], l[p[i]])):
                        sz -= 1
                        mostra_diagonal(l[p[i]], l[st[sz - 1]])
                    else:
                        break
                st[sz] = p[i]
                sz += 1
                update_next(temp_next, l, st[sz - 1], st[sz - 2])
            elif (is_adj(p[i], f, n) and not is_adj(p[i], b, n)):
                print('Case 2')
                aux = b
                while (sz > 1):
                    mostra_diagonal(l[p[i]], l[st[sz - 1]])
                    sz -= 1
                sz -= 1
                st[sz] = aux
                sz += 1
                st[sz] = p[i]
                sz += 1
                update_next(temp_next, l, st[sz - 1], st[sz - 2])
            # elif (is_adj(p[i], f, n) and is_adj(p[i], b, n)):
            else:
                print('Case 3')
                # sz -= 1
                while (sz > 2):
                    sz = sz - 1
                    mostra_diagonal(l[p[i]], l[st[sz - 1]])




            
