#include <reg51.h>
sbit buzz = P1^5;
void delay(unsigned int x);
void main(void)
{
  while (1)
  {
    buzz = 1;
    delay(50);
    buzz = 0;
    delay(100);
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 1275; j++);
}
