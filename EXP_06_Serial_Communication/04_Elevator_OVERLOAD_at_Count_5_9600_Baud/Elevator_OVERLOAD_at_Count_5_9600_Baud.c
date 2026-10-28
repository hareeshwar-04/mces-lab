#include <reg51.h>
void trans(unsigned char x);
void main(void)
{
  unsigned char a[] = "OVERLOAD";
  unsigned char count, i;
  TMOD = 0x20;
  TH1 = 253;
  SCON = 0x50;
  TR1 = 1;
  for (count = 0; count < 5; count++)
  {
  }
  for (i = 0; i < 8; i++)
  {
    trans(a[i]);
  }
  while (1);
}

void trans(unsigned char x)
{
  SBUF = x;
  while (TI == 0);
  TI = 0;
}
