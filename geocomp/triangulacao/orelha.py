#!/usr/bin/env python3

from geocomp.common.polygon import Polygon
from geocomp.common.segment import Segment
from geocomp.common.guiprim import *

""" l pontos do poligono em ordem anti-horaria """
def Orelha(l):
    poly = Polygon(l)
    poly.plot() # tirar isso daqui?
    n = len(l)
    MarcaOrelha(poly, n)
    while n > 3:
        v = poly.pts
        while not v.orelha:
            v = v.next
        v.unhilight()
        u = v.prev
        w = v.next
        MostraDiagonal(u, w)
        u.next = w
        w.prev = u
        poly.pts = w
        n = n - 1
        u.orelha = PontaDeOrelha(poly, n, u)
        if u.orelha:
            u.hilight()
        w.orelha = PontaDeOrelha(poly, n, w)
        if w.orelha:
            w.hilight()

def MostraDiagonal(v, w):
    Segment(v, w).hilight()

""" 
    marca as orelhas do polígono poly de n pontos
    p.orelha = True/False
    para cada ponto p do poligono
"""
def MarcaOrelha(poly, n):
    p = poly.pts
    for _ in range(n):
        p.orelha = PontaDeOrelha(poly, n, p)
        if p.orelha:
            p.hilight()
        p = p.next

def PontaDeOrelha(poly, n, v):
    u = v.prev
    w = v.next
    return Diagonal(poly, n, u, w)

def Diagonal(poly, n, i, j):
    return NoCone(i, j) and QuaseDiagonal(poly, n, i, j)

def QuaseDiagonal(poly, n, i, j):
    k = poly.pts
    for _ in range(n - 1):
        l = k.next
        if k != i and k != j and l != i and l != j:
            if Intersecta(i, j, k, l):
                return False
        k = k.next

    return True

def Entre(a, b, c):
    if not collinear(a, b, c):
        return False
    if a.x != b.x:
        return (a.x <= c.x and c.x <= b.x) or (b.x <= c.x and c.x <= a.x)
    else:
        return (a.y <= c.y and c.y <= b.y) or (b.y <= c.y and c.y <= a.y)

def Intersecta(a, b, c, d):
    if IntersectaProp(a, b, c, d):
        return True
    return Entre(a, b, c) or Entre(a, b, d) or Entre(c, d, a) or Entre(c, d, b)

def IntersectaProp(a, b, c, d):
    if  collinear(a, b, c) or collinear(a, b, d) or collinear(c, d, a) or collinear(c, d, b):
        return False
    return (left(a, b, c) ^ left(a, b, d)) and (left(c, d, a) ^ left(c, d, b))

def NoCone(i, j):
    u = i.prev
    w = i.next
    if left_on(u, i, w):
        return left(i, j, u) and left(j, i, w)
    else:
        return not (left_on(i, j, w) and left_on(j, i, u))
