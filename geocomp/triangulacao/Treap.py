#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import random
from geocomp.common.guiprim import left as esquerda
from geocomp.common.segment import Segment

def random_integer():
    return random.randint(1, 1e9)

def AcendeAresta(e):
    Segment(e.a, e.b).hilight(color_line='purple')

def ApagaAresta(e):
    Segment(e.a, e.b).hilight(color_line='red')

class TreapNode:
    def __init__(self, edge, priority):
        self.edge = edge
        self.priority = priority
        self.left = None
        self.right = None

""" 
Árvore balanceada para guardar a linha de varredura
Guarda segmentos em seus nós, porém recebe um ponto para
comparar com os segmentos na inserção/remoção.
"""
class Treap:
    def __init__(self):
        self._root = None
    
    def _split(self, tree, key):
        if tree == None:
            return (None, None)
        if esquerda(tree.edge.a, tree.edge.b, key): # ponto esta para a esquerda do segmento
            left, tree.left = self._split(tree.left, key)
            return (left, tree)
        else:
            tree.right, right = self._split(tree.right, key)
            return (tree, right)

    def _merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        if left.priority < right.priority:
            right.left = self._merge(left, right.left)
            return right
        else:
            left.right = self._merge(left.right, right)
            return left

    def insert(self, edge, key):
        AcendeAresta(edge)
        node = TreapNode(edge, random_integer())
        left, right = self._split(self._root, key)
        self._root = self._merge(self._merge(left, node), right)

    def _erase_r(self, tree, edge, key):
        if edge == tree.edge:
            return self._merge(tree.left, tree.right)
        if esquerda(tree.edge.a, tree.edge.b, key): # ponto esta para a esquerda do segmento
            tree.left = self._erase_r(tree.left, edge, key)
            return tree
        else:
            tree.right = self._erase_r(tree.right, edge, key)
            return tree

    def erase(self, edge, key):
        ApagaAresta(edge)
        self._root = self._erase_r(self._root, edge, key)

    def _lower_bound_r(self, tree, key):
        if tree == None:
            return None
        if esquerda(tree.edge.a, tree.edge.b, key): # ponto esta para a esquerda do segmento
            return self._lower_bound_r(tree.left, key)
        node = self._lower_bound_r(tree.right, key)
        if node != None:
            return node
        return tree

    def lower_bound(self, key):
        "devolve a maior chave <= key"
        node = self._lower_bound_r(self._root, key)
        if node == None:
            return None
        return node.edge
