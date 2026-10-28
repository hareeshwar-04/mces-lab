#include <reg51.h>
#define step P1
void delay(unsigned int x);
void main(void)
{
  step = 0x00;
  while (1)
  {
    step = 0xF1;
    delay(10);
    step = 0xF2;
    delay(10);
    step = 0xF4;
    delay(10);
    step = 0xF8;
    delay(10);
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 1275; j++);
}
