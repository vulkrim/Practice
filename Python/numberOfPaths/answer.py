#!/usr/bin/python3

def num_of_paths_to(i,j,d):
  if (i,j) in d:
    return d[(i,j)]
  
  counter = 0
  
  if j > 0:
    counter += num_of_paths_to(i,j-1,d)
  
  if j < i:
    counter += num_of_paths_to(i-1,j,d)
  
  d[(i,j)] = counter
  
  return counter
  
def num_of_paths_to_dest(n):
  d = {(0,0): 1}
  return num_of_paths_to(n-1, n-1,d)
