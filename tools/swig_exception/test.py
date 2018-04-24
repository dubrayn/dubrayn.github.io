#!/usr/bin/env python

import sys
import testmod3

a = testmod3.Myclass()
try:
  a.func0(-2.0)

except RuntimeError as e:
  print("runtime error '%s'" % (e))
except:
  print("other error: %s" % (sys.exc_info()[1]))

print('OK')
