#ifndef MYCLASS_H
#define MYCLASS_H

#include <armadillo>

class Myclass
{
  public:
  Myclass(void);
  arma::mat testArma(arma::mat);
  arma::mat getEmptyArma(int n);
};

#endif
