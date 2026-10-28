#include <reg51.h>
sbit wave = P2^4;
void buzz(void);
void serial(void);
void trans(unsigned char y);
void delay(unsigned int x);

void extera_0() interrupt 0
{
  buzz();
  serial();
}

void main(void)
{
  IE = 0x81;
  SCON = 0x50;
  TMOD = 0x20;
  TH1 = 253;
  TR1 = 1;
  while (1);
}

void buzz(void)
{
  wave = 1;
  delay(2000);
  wave = 0;
  delay(1000);
}

void serial(void)
{
  unsigned char a[] = "FIRE";
  unsigned char i;
  for (i = 0; i < 4; i++)
  {
    trans(a[i]);
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 1275; j++);
}

void trans(unsigned char y)
{
  SBUF = y;
  while (TI == 0);
  TI = 0;
}
