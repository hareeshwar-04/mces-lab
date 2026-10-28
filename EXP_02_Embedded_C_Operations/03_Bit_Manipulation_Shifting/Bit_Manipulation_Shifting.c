#include <reg51.h>
void main(void)
{
  P0 = 0x77 & 0x33;
  P1 = 0x77 | 0x33;
  P3 = ~0x77;

  P0 = 0x77 >> 3;
  P1 = 0x33 >> 4;
  P2 = 0x33 << 4;

  while (1);
}
