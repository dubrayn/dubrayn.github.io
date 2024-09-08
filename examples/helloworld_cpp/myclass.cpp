#include "myclass.h"

MyClass::MyClass(int _a) : a(_a)
{
// possible other ways: "a = int(_a);" or "a = _a;"
}

int MyClass::myFunc(int b)
{
  return a + b; // "a" is the same as "this->a"
}
