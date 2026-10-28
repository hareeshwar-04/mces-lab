#include <reg51.h>
void main(void)
{
  unsigned int i;
  for (i = 0; i < 10; i++)
  {
    P1 = 0x55;
    P1 = 0xAA;
  }
  while (1);
}
