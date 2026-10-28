#include <reg51.h>
sbit DC1 = P1^6;
sbit DC2 = P1^7;
void delay(unsigned int x);
void main(void)
{
  while (1)
  {
    DC1 = 0;
    DC2 = 1;
    delay(1000);
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 1275; j++);
}
