#!/usr/bin/env python

import testmod3
import numpy as np

mc = testmod3.Myclass()

a = mc.getEmptyArma(3)
a[0,1] = 1.0
print(a)
print(mc.testArma(a))
