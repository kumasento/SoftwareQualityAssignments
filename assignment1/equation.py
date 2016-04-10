#!/usr/bin/env python

import sys
from math import sqrt

if __name__ == '__main__':
  if len(sys.argv[1:]) != 3:
    print 'Usage: %s [a1] [a2] [a3]' % sys.argv[0]
    exit(1)

  try:
    a1,a2,a3 = map(float, sys.argv[1:4])
    if a1 == 0.0:
      if a2 == 0.0:
        if a3 == 0.0:
          print 'Infinite roots'
        else:
          print 'No root'
      else:
        print -a3/a2
    else:
      delta = a2**2-4*a1*a3
      if delta > 0.0:
        print (-a2-sqrt(delta))/(2*a1), (-a2+sqrt(delta))/(2*a1)
      elif delta == 0.0:
        print (-a2-sqrt(delta))/(2*a1)
      else:
        print 'No root'

  except ValueError as e:
    print e
    exit(1)
