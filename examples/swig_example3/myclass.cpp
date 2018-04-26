#include <iostream>
#include "myclass.h"

Myclass::Myclass(int vala)
{
  a = vala;
}

double Myclass::func0(double x)
{
  return x * x + a;
}

void Myclass::print(int i)
{
  std::cout << i << std::endl;
}
