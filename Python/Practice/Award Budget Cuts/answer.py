#!/usr/bin/python3
def find_grants_cap(grantsArray, budget):
  budget = float(budget)
  average = budget/len(grantsArray)
  belowAverage = [i  for i in grantsArray if i <= average]
  aboveAverage = [i for i in grantsArray if i > average] 
  newBudget = budget - sum(belowAverage)
  newAverage = newBudget/len(aboveAverage)
  if len(aboveAverage) == 0:
    return []
  if min(aboveAverage) > newAverage:
    return max(belowAverage + [newAverage for i in range(len(aboveAverage))])
  if  min(aboveAverage) < newAverage:
    return max(belowAverage + [find_grants_cap(aboveAverage, newBudget)])
