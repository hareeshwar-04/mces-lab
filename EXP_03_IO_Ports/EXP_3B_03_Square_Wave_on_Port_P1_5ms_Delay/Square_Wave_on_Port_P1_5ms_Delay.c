#include <reg51.h>
void delay(void);
void main(void)
{
  while (1)
  {
    P1 = 0x00;
    delay();
    P1 = 0x7F;
    delay();
    P1 = 0xFF;
    delay();
  }
}

void delay(void)
{
  unsigned int x;
  for (x = 0; x < 133; x++);
}
