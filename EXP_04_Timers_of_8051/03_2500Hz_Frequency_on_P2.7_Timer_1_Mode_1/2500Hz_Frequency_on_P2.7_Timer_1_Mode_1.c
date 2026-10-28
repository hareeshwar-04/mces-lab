#include <reg51.h>
sbit wave = P2^7;
void delay(void);
void main(void)
{
  while (1)
  {
    wave = 1;
    delay();
    wave = 0;
    delay();
  }
}

void delay(void)
{
  TMOD = 0x10;
  TL1 = 0x48;
  TH1 = 0xFF;
  TR1 = 1;
  while (TF1 == 0);
  TR1 = 0;
  TF1 = 0;
}
