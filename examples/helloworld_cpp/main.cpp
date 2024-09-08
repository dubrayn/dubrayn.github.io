#include "myclass.h"

#include <iostream>

int main(int charc, char** argv)
{
  MyClass myClass(2);

  std::cout << "Result: " << myClass.myFunc(3);
  std::cout << std::endl;

  return 0;
}
