#include <reg51.h>
sbit P3_6 = P3^6;
void main(void)
{
  P3_6 = 1; // Configure P3.6 as input
  while (1)
  {
    if (P3_6 == 1)
    {
      P1 = 0x55;
      P2 = 0xAA;
    }
    else
    {
      P1 = 0xAA;
      P2 = 0x55;
    }
  }
}
