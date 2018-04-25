#include <iostream>

double func0(int a, int b) throw(int, double)
{
  if (b == 0) // hit
  {
    throw 'b';  // throw a char
  }
  return (double)a / (double)b;
}

int main(int argc, char ** argv)
{
  try
  {
    double v0 = func0(3, 1);
    double v1 = func0(2, 0);
    double v2 = func0(5, 2);
  }
  
  catch(int a)  // catch
  {
    std::cout << "division by zero error" << std::endl; // handle
  }
  return 0;
}
