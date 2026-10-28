#include <reg51.h>
#define sel P1
#define disp P2
void delay(unsigned int x);
void main(void)
{
  while (1)
  {
    sel = 0x00;
    disp = 0x79;
    delay(1);
    sel = 0x10;
    disp = 0x3E;
    delay(1);
    sel = 0x20;
    disp = 0x38;
    delay(1);
    sel = 0x30;
    disp = 0x07;
    delay(1);
    sel = 0x40;
    disp = 0x07;
    delay(1);
    sel = 0x50;
    disp = 0x5B;
    delay(1);
  }
}

void delay(unsigned int x)
{
  unsigned int i, j;
  for (i = 0; i < x; i++)
    for (j = 0; j < 30; j++);
}
