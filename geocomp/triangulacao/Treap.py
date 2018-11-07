#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import random

def random_integer():
    return random.randint(1, 1e9)

class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self._root = None
    
    def _split(self, tree, key):
        if tree == None:
            return (None, None)
        if key < tree.key:
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

    def contains(self, key):
        node = self._root
        while node != None:
            if key == node.key:
                return True
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, key):
        if not self.contains(key):
            node = TreapNode(key, random_integer())
            left, right = self._split(self._root, key)
            self._root = self._merge(self._merge(left, node), right)

    def _erase_r(self, tree, key):
        if key == tree.key:
            return self._merge(tree.left, tree.right)
        if key < tree.key:
            tree.left = self._erase_r(tree.left, key)
            return tree
        else:
            tree.right = self._erase_r(tree.right, key)
            return tree

    def erase(self, key):
        if self.contains(key):
            self._root = self._erase_r(self._root, key)

    def _lower_bound_r(self, tree, key):
        if tree == None:
            return None
        if key < tree.key: #key == tree.key tambem?
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
        return node.key


if __name__ == '__main__':
    t = Treap()
    t.insert(1)
    t.insert(2)
    t.insert(6)
    assert t.contains(2)
    assert not t.contains(4)
    t.erase(2)
    assert not t.contains(2)
    assert t.contains(6)
    assert t.lower_bound(7) == 6
    assert t.lower_bound(6) == 6
    assert t.lower_bound(5) == 1
    t.insert(2)
    assert t.lower_bound(5) == 2
    print("ok!")
