#include <reg51.h>
void trans(unsigned char x);
void main(void)
{
  unsigned char a[] = "24B81A7700";
  unsigned char i;
  TMOD = 0x20;
  SCON = 0x50;
  TH1 = 244;
  TR1 = 1;
  while (1)
  {
    for (i = 0; i < 10; i++)
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
