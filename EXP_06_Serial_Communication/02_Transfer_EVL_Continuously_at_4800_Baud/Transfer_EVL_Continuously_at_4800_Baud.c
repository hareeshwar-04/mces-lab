#include <reg51.h>
void trans(unsigned char x);
void main(void)
{
  unsigned char a[] = "EVL ";
  unsigned char i;
  TMOD = 0x20;
  SCON = 0x50;
  TH1 = 250;
  TR1 = 1;
  while (1)
  {
    for (i = 0; i < 4; i++)
    {
      trans(a[i]);
    }
  }
}

void trans(unsigned char x)
{
  SBUF = x;
  while (TI == 0);
  TI = 0;
}
