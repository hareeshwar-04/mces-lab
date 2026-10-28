#include <reg51.h>
void main(void)
{
  unsigned char x = 0x45, y = 0x18;
  unsigned char add, sub, mul, div, rem;

  add = x + y;
  sub = x - y;
  mul = x * y;
  div = x / y;
  rem = x % y;

  while (1);
}
