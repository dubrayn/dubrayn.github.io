#include <iostream>

double func1(int a, int b) { if (a == 0) throw 3; return 0.0; }

double func0(int a, int b)
{
  double r = 0.0;
  try
  {
    r = func1(0, b);
    std::cout << "normal execution" << std::endl;
  }
  catch(int &i)
  {
    std::cout << "catch in func0" << std::endl;
    throw;
  }
  return r;
}

int main(int argc, char ** argv)
{
  try { func0(0,1); }
  catch(int &i) { std::cout << "catch in main" << std::endl; }
  return 0;
}
