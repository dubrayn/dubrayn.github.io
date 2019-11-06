#!/usr/bin/env python3

import testmod3
import numpy as np

numpyArray = np.array([[0.1, 0.2], [0.3, 0.4]], dtype = np.float64, order = 'F')
print("Initial object:")
print(numpyArray)

mc = testmod3.Myclass(numpyArray)
print("Object in the C++ class (constructor with argument):")
print(mc.myMat)

mc = testmod3.Myclass()
print("Object in the C++ class (empty constructor):")
print(mc.myMat)


a = mc.getEmptyArma(3)
a[0,1] = 1.0
print("Object returned by the C++ method getEmptyArma() and modified:")
print(a)

print("Object returned by the C++ method testArma() (transposition):")
print(mc.testArma(a))
