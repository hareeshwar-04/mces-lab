#include <reg51.h>
#define DAC P1

void delay(unsigned int x);

void main(void)
{
  DAC = 0x00;
  while (1)
  {
    unsigned int i;
    for (i = 0; i < 255; i++)
    {
      DAC = (unsigned char)i;
      delay(1);
    }
    for (i = 255; i > 0; i--)
    {
      DAC = (unsigned char)i;
      delay(1);
    }
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 1275; j++);
}
