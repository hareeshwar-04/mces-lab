#include <reg51.h>
sbit wave1 = P1^2;
sbit wave2 = P2^4;

void timer0() interrupt 1
{
  wave1 = ~wave1;
  TL0 = 0x33;
  TH0 = 0xFE;
}

void timer1() interrupt 3
{
  wave2 = ~wave2;
  TL1 = 0xCD;
  TH1 = 0xF8;
}

void main(void)
{
  IE = 0x8A;
  TMOD = 0x11;
  TL0 = 0x33;
  TH0 = 0xFE;
  TL1 = 0xCD;
  TH1 = 0xF8;
  wave1 = 1;
  wave2 = 1;
  TR1 = 1;
  TR0 = 1;
  while (1);
}
