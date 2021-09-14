#include "solver.h"

int main(int, char**)
{
  Solver solver(2);

  auto result = solver.calc();

  result.print("result");
}
