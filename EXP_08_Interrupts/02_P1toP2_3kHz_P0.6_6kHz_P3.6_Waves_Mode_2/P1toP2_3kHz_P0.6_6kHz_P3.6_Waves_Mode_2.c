#include <reg51.h>
sbit wave1 = P0^6;
sbit wave2 = P3^6;

void timer0() interrupt 1
{
  wave1 = ~wave1;
  TH0 = 0x68;
}

void timer1() interrupt 3
{
  wave2 = ~wave2;
  TH1 = 0xB4;
}

void main(void)
{
  IE = 0x8A;
  TMOD = 0x22;
  TH0 = 0x68;
  TH1 = 0xB4;
  wave1 = 1;
  wave2 = 1;
  TR1 = 1;
  TR0 = 1;
  while (1)
  {
    P2 = P1;
  }
}
