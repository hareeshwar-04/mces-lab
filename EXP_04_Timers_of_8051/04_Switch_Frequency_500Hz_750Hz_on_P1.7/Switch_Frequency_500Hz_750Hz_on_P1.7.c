#include <reg51.h>
sbit sw = P1^2;
sbit OUT = P1^7;
void delay500(void);
void delay750(void);
void main(void)
{
  while (1)
  {
    if (sw == 0)
    {
      OUT = 1;
      delay500();
      OUT = 0;
      delay500();
    }
    else
    {
      OUT = 1;
      delay750();
      OUT = 0;
      delay750();
    }
  }
}

void delay500(void)
{
  TMOD = 0x00;
  TH0 = 0xC6;
  TL0 = 0x0C;
  TR0 = 1;
  while (TF0 == 0);
  TR0 = 0;
  TF0 = 0;
}

void delay750(void)
{
  TMOD = 0x00;
  TH0 = 0x0A;
  TL0 = 0x11;
  TR0 = 1;
  while (TF0 == 0);
  TR0 = 0;
  TF0 = 0;
}
