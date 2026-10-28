#include <reg51.h>
#define DAC P1

void delay(unsigned int x);

void main(void)
{
  while (1)
  {
    DAC = 0x00;
    delay(1000);
    DAC = 0xFF;
    delay(1000);
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 1275; j++);
}
