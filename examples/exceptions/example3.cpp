#include <iostream>

double func0(int a, int b) throw(int, char, double)
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
    double v1 = func0(2, 0);
  }

  catch(char &c)  // catch
  {
    std::cout << "catch char exception" << std::endl; // handle
  }
  return 0;
}
