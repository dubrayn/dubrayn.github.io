#!/usr/bin/env python

class myLookupErrorClass(LookupError):
  '''raise this class in case of a lookup error'''

try:
  raise myLookupErrorClass('custom message')
except myLookupErrorClass as e:
  print("catch myLookupErrorClass: %s" % (str(e)))
except:
  print("generic catch")

  

