#include <reg51.h>
void main(void)
{
  unsigned char x = 0x77, y = 0x33;
  unsigned char add1, sub1, div1, rem1, inc1, dec1;
  unsigned int mul1;

  add1 = x + y;
  sub1 = x - y;
  div1 = x / y;
  rem1 = x % y;
  mul1 = x * y;
  inc1 = x + 1;
  dec1 = x - 1;

  while (1);
}
