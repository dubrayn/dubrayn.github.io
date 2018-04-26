#include "stdlib.h"
#include "stdio.h"

#define SIZE 3

int main(int argc, char **argv)
{
  int* table = (int*)malloc(sizeof(int) * SIZE);

  for (int i = 0; i < SIZE; i++)
  {
    table[i] = i;
  }

  for (int i = 0; i < SIZE; i++)
  {
    printf("table[%d]=%d\n", i, table[i]);
  }

  free(table); 

  return 0;
}
