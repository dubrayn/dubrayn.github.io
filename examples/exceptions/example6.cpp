#include <iostream>
#include <exception>

int main(int argc, char ** argv)
{
  try
  {
    int* myarray= new int[10000000000];
  }
  catch(std::exception &e)
  {
    std::cout << "catch exception, what(): " << e.what() << std::endl;
  }
  return 0;
}

