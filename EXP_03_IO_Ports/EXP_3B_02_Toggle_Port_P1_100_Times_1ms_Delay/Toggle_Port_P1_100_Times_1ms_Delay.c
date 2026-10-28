#include <reg51.h>
void delay(void);
void main(void)
{
  unsigned int i;
  for (i = 0; i < 100; i++)
  {
    P1 = 0x55;
    delay();
    P1 = 0xAA;
    delay();
  }
  while (1);
}

void delay(void)
{
  unsigned int x;
  for (x = 0; x < 133; x++);
}
