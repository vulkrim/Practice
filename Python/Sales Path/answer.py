#!/usr/bin/python3

def get_cheapest_cost(rootNode, cost=0):
  if not rootNode.children:
    return rootNode.cost + cost
  return min([get_cheapest_cost(child, cost + rootNode.cost) for child in rootNode.children])

class Node:

    def __init__(self, cost, parent=None):
    self.cost = cost
    self.children = []
    self.parent = None
  
