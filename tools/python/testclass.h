#ifndef TESTCLASS_H
#define TESTCLASS_H

#include "armadillo"

class TestClass
{
  public:
  TestClass(int, int);
  void init0(void);
  void init1(void);
  double func0(void);
  int dim0;
  int dim1;
  arma::mat a;
  arma::mat b;
};

#endif
