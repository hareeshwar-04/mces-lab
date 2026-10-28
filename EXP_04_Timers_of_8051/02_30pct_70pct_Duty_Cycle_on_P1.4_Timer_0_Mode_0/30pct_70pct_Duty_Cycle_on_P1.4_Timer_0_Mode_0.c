#include <reg51.h>
sbit wave = P1^4;
void delay1(void);
void delay2(void);
void main(void)
{
  while (1)
  {
    wave = 1;
    delay1();
    wave = 0;
    delay2();
  }
}

void delay1(void)
{
  TMOD = 0x00;
  TL0 = 0x13;
  TH0 = 0xA9;
  TR0 = 1;
  while (TF0 == 0);
  TR0 = 0;
  TF0 = 0;
}

void delay2(void)
{
  TMOD = 0x00;
  TL0 = 0x0D;
  TH0 = 0x36;
  TR0 = 1;
  while (TF0 == 0);
  TR0 = 0;
  TF0 = 0;
}
