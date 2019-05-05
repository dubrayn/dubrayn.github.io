#!/usr/bin/env python

import testmod3
import numpy as np

numpyArray = np.array([[1, 0], [0, 1]], dtype = np.float64, order = 'F')

mc = testmod3.Myclass(numpyArray)
print(mc.myMat)

mc = testmod3.Myclass()
print(mc.myMat)


a = mc.getEmptyArma(3)
a[0,1] = 1.0
print(a)
print(mc.testArma(a))
