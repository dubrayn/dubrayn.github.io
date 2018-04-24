#include <iostream>
#include "myclass.h"

Myclass::Myclass(int vala)
{
  a = vala;
}

double Myclass::func0(double x)
{
  if (x < 0.0)
  {
   throw std::runtime_error("EXCEPTION !!!");
  }
  return x * x + a;
}

void Myclass::print(int i)
{
  std::cout << i << std::endl;
}
