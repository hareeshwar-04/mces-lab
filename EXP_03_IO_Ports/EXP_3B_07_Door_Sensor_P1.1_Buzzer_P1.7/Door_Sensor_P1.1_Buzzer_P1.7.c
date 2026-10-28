#include <reg51.h>
sbit door_sensor = P1^1;
sbit buzzer = P1^7;
void delay(void);
void main(void)
{
  while (1)
  {
    if (door_sensor == 1)
    {
      buzzer = 1;
      delay();
      buzzer = 0;
      delay();
    }
    else
    {
      buzzer = 0;
    }
  }
}

void delay(void)
{
  unsigned int x;
  for (x = 0; x < 133; x++);
}
