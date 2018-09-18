#!/usr/bin/python3

def get_cheapest_cost(rootNode, cost=0):
  if not rootNode.children:
    return rootNode.cost + cost
  return min([get_cheapest_cost(child, cost + rootNode.cost) for child in rootNode.children])
  
