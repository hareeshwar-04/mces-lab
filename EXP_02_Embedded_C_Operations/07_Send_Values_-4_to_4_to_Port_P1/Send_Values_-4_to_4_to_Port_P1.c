#include <reg51.h>
void main(void)
{
  char i;
  for (i = -4; i <= 4; i++)
  {
    P1 = i;
  }
  while (1);
}
