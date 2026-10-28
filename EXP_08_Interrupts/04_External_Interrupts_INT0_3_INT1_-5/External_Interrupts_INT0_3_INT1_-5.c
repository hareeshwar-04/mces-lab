#include <reg51.h>
unsigned char count = 0;
void delay(void);

void externa_0() interrupt 0
{
  count = count + 3;
  P1 = count;
  delay();
}

void externa_1() interrupt 2
{
  count = count - 5;
  P1 = count;
  delay();
}

void main(void)
{
  P1 = 0x00;
  IE = 0x85;
  while (1);
}

void delay(void)
{
  unsigned int i, j;
  for (i = 0; i < 5000; i++)
    for (j = 0; j < 1275; j++);
}
