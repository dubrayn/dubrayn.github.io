#include <armadillo>

int main(int, char**)
{
  arma::wall_clock wclock;

  wclock.tic();

  sleep(1); // do some stuff

  double length = wclock.toc();

  std::cout << "total time: " << length << " [s]" << std::endl;

  return 0;
}
