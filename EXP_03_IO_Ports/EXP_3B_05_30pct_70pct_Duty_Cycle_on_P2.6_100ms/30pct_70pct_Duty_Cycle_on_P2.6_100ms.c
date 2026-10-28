#include <reg51.h>
sbit P = P2^6;
void delay(unsigned char x);
void main(void)
{
  while (1)
  {
    P = 0;
    delay(70);
    P = 1;
    delay(30);
  }
}

void delay(unsigned char x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
  {
    for (j = 0; j < 127; j++);
  }
}
