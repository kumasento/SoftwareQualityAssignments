#!/usr/bin/env python

import sys
import math

def solve(a1, a2, a3):
  assert_params_float(a1,a2,a3)

  if a1 != 0.0:
    delta = a2**2 - 4*a1*a3
    if delta < 0:
      return None
    elif delta == 0:
      return (-a2+math.sqrt(delta))/(2*a1)
    else:
      r1 = (-a2+math.sqrt(delta))/(2*a1)
      r2 = (-a2-math.sqrt(delta))/(2*a1)
      return (r1,r2)
  else:
    if a2 != 0.0:
      return -a3/a2
    else:
      if a3 != 0.0:
        return None
      else:
        return 0.0

def assert_params_float(a1, a2, a3):
  # Check type of input value
  assert type(a1) is float, 'a1 should have float type'
  assert type(a2) is float, 'a2 should have float type'
  assert type(a3) is float, 'a3 should have float type'

def usage():
  print 'Equation Solver'
  print 'Author: Vincent Zhao <vincentzhaorz@gmail.com>'
  print 'Date: 2016.05.02'
  print ''
  print 'usage: %s <a1:float> <a2:float> <a3:float>' % sys.argv[0]

if __name__ == '__main__':

  if len(sys.argv) < 4:
    usage()
    exit(1)

  try:
    a1 = float(sys.argv[1])
    a2 = float(sys.argv[2])
    a3 = float(sys.argv[3])

    print solve(a1,a2,a3)
  except ValueError as e:
    print e
    exit(1)
