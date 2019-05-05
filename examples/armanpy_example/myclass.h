#ifndef MYCLASS_H
#define MYCLASS_H

#include <armadillo>

class Myclass
{
  public:
  Myclass(arma::mat _mat = arma::mat());
  arma::mat testArma(arma::mat);
  arma::mat getEmptyArma(int n);
  arma::mat myMat;
};

#endif
