#include <iostream>
#include <exception>

int func0(int a, int b) throw(int) // non-int exceptions from this function will trigger std::unexpected.
{
  throw 5;
}

void customUnexpected(void)
{
  std::cerr << "unexpected called" << std::endl;
  throw 0; // must throw something or terminate the program
}

int main (void)
{
  std::set_unexpected(customUnexpected);

  try { func0(2, 3); }
  catch(int &i) { std::cout << "catch in main" << std::endl; }
  return 0;
}

