#include <iostream>
#include <exception>
#include <stdexcept>

class A {};
 
class myException: public A, public std::runtime_error
{
  public:
  myException(std::string _mesg = "") : std::runtime_error(_mesg) {};
};

int main(int argc, char ** argv)
{
  try { throw myException("custom text"); }
  catch(std::runtime_error &e) { std::cout << "catch std::runtime_error, what(): " << e.what() << std::endl; }
  catch(myException &e) { std::cout << "catch custom exception, what(): " << e.what() << std::endl; }
  return 0;
}

