#include <reg51.h>
sbit wave = P1^5;
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
  unsigned int i;
  TMOD = 0x02;
  TH0 = 0x1A;
  for (i = 0; i < 1000; i++)
  {
    TR0 = 1;
    while (TF0 == 0);
    TR0 = 0;
    TF0 = 0;
  }
}
