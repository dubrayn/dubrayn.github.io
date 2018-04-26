#include "testclass.h"

int main(int argc, char **argv)
{
  TestClass c(3000, 3000);
  c.init0();
  printf("%e\n", c.func0());
  return 0;
}
