#include <reg51.h>
sbit P3_5 = P3^5;
void main(void)
{
  TMOD = 0x60;
  TH1 = 0x00;
  P3_5 = 1;
  while (1)
  {
    TR1 = 1;
    while (TF1 == 0)
    {
      P2 = TL1;
    }
    TR1 = 0;
    TF1 = 0;
  }
}
