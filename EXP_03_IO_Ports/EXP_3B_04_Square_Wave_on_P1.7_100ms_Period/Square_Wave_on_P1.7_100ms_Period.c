#include <reg51.h>
sbit P = P1^7;
void delay(void);
void main(void)
{
  while (1)
  {
    P = 0;
    delay();
    P = 1;
    delay();
  }
}

void delay(void)
{
  unsigned int x, y;
  for (x = 0; x < 100; x++)
  {
    for (y = 0; y < 133; y++);
  }
}
