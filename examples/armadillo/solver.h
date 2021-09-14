#ifndef SOLVER_H
#define SOLVER_H

#include <armadillo>

class Solver
{
  public:

  Solver(double _factor = 1);

  arma::mat calc(void);

  private:

  double factor = 1.0;
};

#endif
