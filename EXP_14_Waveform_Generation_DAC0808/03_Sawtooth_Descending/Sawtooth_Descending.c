#include <reg51.h>
#define DAC P1

void delay(unsigned int x);

void main(void)
{
  DAC = 0x00;
  while (1)
  {
    int i;
    for (i = 255; i >= 0; i--)
    {
      DAC = (unsigned char)i;
    }
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 1275; j++);
}
