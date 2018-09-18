#!/usr/bin/python3

import collections

def flatten_dictionary(dictionary, parent_key = '', sep = '.'):

  items = []
  for k, v in dictionary.items():
    if len(k) == 0:
      new_key = parent_key
    new_key = parent_key + sep + k if parent_key else k
    if isinstance(v, dict):#collections.MutableMapping):
      items.extend(flatten_dictionary(v, new_key, sep=sep).items())
    else:
      if len(k) == 0:
        new_key = parent_key
      items.append((new_key, v))
  return dict(items)
