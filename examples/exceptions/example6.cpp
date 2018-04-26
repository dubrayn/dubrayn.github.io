#include <iostream>
#include <exception>
#include <stdexcept>

class myException: public std::exception
{
  public:
  myException(std::string _mesg = "")
  {
    mesg = _mesg;
  }
  const char * what(void)
  {
    return mesg.c_str();    
  }
  std::string mesg;
};

int main(int argc, char ** argv)
{
  try
  {
    throw myException("custom text");
  }
  catch(myException &e)
  {
   std::cout << "Custom exception, what(): " << e.what() << std::endl;
  }
  return 0;
}

