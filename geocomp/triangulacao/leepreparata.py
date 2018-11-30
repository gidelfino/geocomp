""" Com base na secao 3.2 do livro de Berg """

from geocomp.common.polygon import Polygon
from geocomp.common.segment import Segment
from geocomp.common.guiprim import *
from functools import cmp_to_key
from geocomp.triangulacao.Treap import Treap
from geocomp.triangulacao.DCEL import DCEL
from geocomp.common.control import *
from geocomp.triangulacao.ymonotono import YMonotono

def MostraDiagonal(p, q):
    Segment(p, q).hilight(color_line='white')


""" 
Uma aresta do poligono que intersecta a linha de varredura 
A aresta é orientada de baixo para cima.
    b
    ^
    |
    |
    |
    a
"""
class SweepLineEdge:
    def __init__(self, a, b):
        if a.y > b.y or (a.y == b.y and a.x < b.x):
            self.a = b
            self.b = a
        else:
            self.a = a
            self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((self.a.x, self.a.y, self.b.x, self.b.y))

def Below(p, q):
    "Um ponto p esta abaixo de um ponto q se p.y < q.y ou p.y = q.y e p.x > q.x"
    if p.y != q.y:
        return p.y < q.y
    return p.x > q.x

def Above(p, q):
    "Um ponto p esta acima de um ponto q se p.y > q.y ou p.y = q.y e p.x < q.x"
    if p.y != q.y:
        return p.y > q.y
    return p.x < q.x

def Start(v):
    "Um vertice v eh start se seus dois vizinhos estao abaixo e o angulo interior em v eh < pi"
    u = v.prev
    w = v.next
    return Below(u, v) and Below(w, v) and left(v, w, u)

def End(v):
    "Um vertice v eh end se seus dois vizinhos estao acima e o angulo interior em v eh < pi"
    u = v.prev
    w = v.next
    return Above(u, v) and Above(w, v) and left(v, w, u)

def Split(v):
    "Um vertice v eh split se seus dois vizinhos estao abaixo e o angulo interior em v eh > pi"
    u = v.prev
    w = v.next
    return Below(u, v) and Below(w, v) and not left(v, w, u)

def Merge(v):
    "Um vertice v eh merge se seus dois vizinhos estao acima e o angulo interior em v eh > pi"
    u = v.prev
    w = v.next
    return Above(u, v) and Above(w, v) and not left(v, w, u)

def HandleStartVertex(v, helper, T, D):
    e = SweepLineEdge(v, v.next)
    T.insert(e, v)
    helper[e] = v

def HandleEndVertex(v, helper, T, D):
    e = SweepLineEdge(v.prev, v)
    if Merge(helper[e]):
        MostraDiagonal(v, helper[e])
        D.add_edge(v, helper[e])
    T.erase(e, v)

def HandleSplitVertex(v, helper, T, D):
    e = T.lower_bound(v)
    MostraDiagonal(v, helper[e])
    D.add_edge(v, helper[e])
    helper[e] = v
    e = SweepLineEdge(v, v.next)
    T.insert(e, v)
    helper[e] = v

def HandleMergeVertex(v, helper, T, D):
    e = SweepLineEdge(v.prev, v)
    if Merge(helper[e]):
        MostraDiagonal(v, helper[e])
        D.add_edge(v, helper[e])
    T.erase(e, v)
    e = T.lower_bound(v)
    if Merge(helper[e]):
        MostraDiagonal(v, helper[e])
        D.add_edge(v, helper[e])
    helper[e] = v

def HandleRegularVertex(v, helper, T, D):
    if Below(v, v.prev): # interior do poligono esta a direta de v
        e = SweepLineEdge(v.prev, v)
        if Merge(helper[e]):
            MostraDiagonal(v, helper[e])
            D.add_edge(v, helper[e])
        T.erase(e, v)
        e = SweepLineEdge(v, v.next)
        T.insert(e, v)
        helper[e] = v
    else:
        e = T.lower_bound(v)
        if Merge(helper[e]):
            MostraDiagonal(v, helper[e])
            D.add_edge(v, helper[e])
        helper[e] = v

def MostraSweep(p):
    id = plot_horiz_line(p.y)
    control.sleep()
    return id

def EscondeSweep(id):
    plot_delete(id)

def Events(poly, n):
    p = poly.pts
    Q = []
    for _ in range(n):
        Q.append(p)
        p = p.next
    def cmp(p, q):
        if p.y != q.y:
            return q.y - p.y
        return p.x - q.x
    Q.sort(key = cmp_to_key(cmp))
    return Q

def LeePreparata(l):
    poly = Polygon(l)
    poly.plot()
    n = len(l)
    Q = Events(poly, n)
    T = Treap()
    D = DCEL(poly)
    helper = {}
    for p in Q:
        sweep_id = MostraSweep(p)
        if Start(p):
            HandleStartVertex(p, helper, T, D)
        elif End(p):
            HandleEndVertex(p, helper, T, D)
        elif Split(p):
            HandleSplitVertex(p, helper, T, D)
        elif Merge(p):
            HandleMergeVertex(p, helper, T, D)
        else:
            HandleRegularVertex(p, helper, T, D)
        EscondeSweep(sweep_id)

    for poly in D.to_polygons():
        YMonotono(poly, print_polygon=False)