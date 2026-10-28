#include <reg51.h>
sbit led = P1^4;
void delay(unsigned int x);
void main(void)
{
  while (1)
  {
    led = 1;
    delay(500);
    led = 0;
    delay(500);
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 1275; j++);
}
