#include "solver.h"

Solver::Solver(double _factor) : factor(_factor)
{
}

arma::mat Solver::calc(void)
{
  arma::mat result;

  arma::mat A = {{1, 2}, {3, 4}}; // C++11
  arma::mat B = {{5, 6}, {7, 8}}; // C++11

  result = factor * A * B.t();

  return result;
}

