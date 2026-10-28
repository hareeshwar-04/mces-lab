#include <reg51.h>
sbit bit1 = P3^3;
void main(void)
{
  unsigned int i;
  for (i = 0; i < 50000; i++)
  {
    bit1 = ~bit1;
  }
  while (1);
}
