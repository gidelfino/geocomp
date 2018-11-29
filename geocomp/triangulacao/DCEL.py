#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from geocomp.common.polygon import Polygon
from geocomp.common.prim import *

""" Devolve se dois pontos sao iguais
Nao implementamos na classe Point para nao mexer no framework """
def same_point(p, q):
    return p.x == q.x and p.y == q.y

class _HalfEdge:
    def __init__(self, v):
        self.origin = v
        self.twin = None
        self.prev = None
        self.next = None

    def to(self):
        return self.twin.origin

    def __str__(self):
        return 'origin %s, to %s' % (self.origin, self.twin.origin)

    def __eq__(self, other):
        return same_point(self.origin, other.origin) and same_point(self.twin.origin, other.twin.origin)

    def __hash__(self):
        return hash((self.origin.x, self.origin.y, self.twin.origin.x, self.twin.origin.y))

""" Devolve o par de meia-arestas vw, wv """
def create_half_edges(v, w):
    vw = _HalfEdge(v)
    wv = _HalfEdge(w)
    vw.twin = wv
    wv.twin = vw
    return vw, wv

def NoCone(prv, cur, e):
    u = cur.to()
    w = prv.to()
    i = e.to()
    j = e.origin
    if left_on(u, i, w):
        return left(i, j, u) and left(j, i, w)
    else:
        return not (left_on(i, j, w) and left_on(j, i, u))

class DCEL:
    """ Cria uma DCEL a partir do poligono poly """
    def __init__(self, poly):
        self.leaving = {}
        half_edges = []
        v = poly.pts
        while True: # oh python, pq vc nao tem do while?
            w = v.next
            vw, wv = create_half_edges(v, w)
            self.leaving[v] = vw
            half_edges.append(vw)
            v = w
            if v == poly.pts:
                break
        n = len(half_edges)
        for i in range(n):
            half_edges[i].prev = half_edges[(n + i - 1) % n]
            half_edges[i].next = half_edges[(i + 1) % n]
            half_edges[i].twin.prev = half_edges[(i + 1) % n].twin
            half_edges[i].twin.next = half_edges[(n + i - 1) % n].twin

    """ Devolve a proxima meia-aresta incidente a v (e = vw), no sentido anti-horario """
    def _next_half_edge(self, e):
        prv = self.leaving[e.to()]
        cur = prv.prev.twin
        while True:
            if NoCone(prv, cur, e):
                return prv
            prv = cur
            cur = cur.prev.twin

    """ adiciona a digonal vw. """
    def add_edge(self, v, w):
        vw, wv = create_half_edges(v, w)

        vw_next = self._next_half_edge(vw)
        wv_next = self._next_half_edge(wv)
        vw_prev = wv_next.prev
        wv_prev = vw_next.prev

        vw.next = vw_next
        vw.prev = vw_prev
        vw.next.prev = vw
        vw.prev.next = vw

        wv.next = wv_next
        wv.prev = wv_prev
        wv.next.prev = wv
        wv.prev.next = wv

    """ Devolve uma lista de poligonos induzidos pelas faces internas da DCEL """
    def to_polygons(self):
        polygons = []
        seen = {}
        for _, half_edge in self.leaving.items():
            current = half_edge
            if current in seen:
                continue
            seen[current] = True
            polygon = [current.origin]
            current = current.next
            while current != half_edge:
                seen[current] = True
                polygon.append(current.origin)
                current = current.next
            polygons.append(polygon)
        return polygons





