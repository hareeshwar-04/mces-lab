#include <reg51.h>
void main(void)
{
  unsigned char x = 0x77, y = 0x33;
  unsigned char and1, or1, xor1, not1;

  and1 = x & y;
  or1  = x | y;
  xor1 = x ^ y;
  not1 = ~x;

  P0 = and1;
  P1 = or1;
  P2 = xor1;
  P3 = not1;

  while (1);
}
