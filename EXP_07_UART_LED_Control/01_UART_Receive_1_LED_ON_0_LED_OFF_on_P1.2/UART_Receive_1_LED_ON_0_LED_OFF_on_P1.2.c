#include <reg51.h>
sbit k = P1^2;
void main(void)
{
  unsigned char a;
  TMOD = 0x20;
  SCON = 0x50;
  TH1 = 253;
  TR1 = 1;
  P1 = 0x00;
  while (1)
  {
    while (RI == 0);
    a = SBUF;
    RI = 0;
    if (a == '1')
      k = 1;
    else
      k = 0;
  }
}
