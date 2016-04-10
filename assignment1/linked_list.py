#!/usr/bin/env python

import sys

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print 'Usage: %s [index]' % sys.argv[0]

  try:
    x = int(sys.argv[1])
    if x < 0:
      raise IndexError('index should not be negative')
    l = range(10)
    print l[x]
  except ValueError as e:
    print e
    exit(1)
  except IndexError as e:
    print e
    exit(1)
