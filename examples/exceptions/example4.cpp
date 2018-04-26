#include <iostream>
#include <exception>

int func0(int a, int b) noexcept
{
  throw 42;
}

int main(int argc, char ** argv)
{
  try
  {
    func0(0, 0);
  }
  catch(int &i)
  {
    std::cout << "catch int exception" << std::endl;
  }
  return 0;
}

