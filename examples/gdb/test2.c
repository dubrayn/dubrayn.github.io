#include "stdlib.h"
#include "stdio.h"

// new function
int addition(int a, int b)
{
  return a + b;
}

#define SIZE 3

int main(int argc, char **argv)
{
  for (int i = 0; i < SIZE; i++)
  {
    printf("i=%d i+3=%d\n", i, addition(i, 3));
  }

  return 0;
}
