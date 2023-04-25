#include "myclass.h"

Myclass::Myclass(arma::mat _mat) : myMat(_mat)
{
}

arma::mat Myclass::testArma(arma::mat A)
{
  return A.t();
}

arma::mat Myclass::getEmptyArma(int n)
{
  return arma::zeros(n, n);
}
