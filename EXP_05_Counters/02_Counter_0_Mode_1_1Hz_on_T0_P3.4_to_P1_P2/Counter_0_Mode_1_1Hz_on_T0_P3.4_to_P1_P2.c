#include <reg51.h>
sbit P3_4 = P3^4;
void main(void)
{
  P3_4 = 1;
  TMOD = 0x05;
  TL0 = 0;
  TH0 = 0;
  while (1)
  {
    do
    {
      TR0 = 1;
      P1 = TL0;
      P2 = TH0;
    } while (TF0 == 0);
    TR0 = 0;
    TF0 = 0;
  }
}
