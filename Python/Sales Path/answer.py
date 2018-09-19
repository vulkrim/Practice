#!/usr/bin/python3



def get_cheapest_cost(qDictionary,node='root', cost=0):

    if not qDictionary[node]['child']:
        return qDictionary[node]['value'] + cost
    return min([get_cheapest_cost(
            qDictionary,
            child,
            qDictionary[node]['value'] + cost)
            for child in qDictionary[node]['child']])



'''
#used with transversing nodes

def get_cheapest_cost(rootNode, cost=0):
  if not rootNode.children:
    return rootNode.cost + cost
  return min([get_cheapest_cost(child, cost + rootNode.cost) for child in rootNode.children])

class Node:

    def __init__(self, cost, parent=None):
    self.cost = cost
    self.children = []
    self.parent = None
'''

