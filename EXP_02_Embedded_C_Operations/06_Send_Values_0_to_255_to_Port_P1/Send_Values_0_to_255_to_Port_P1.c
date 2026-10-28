#include <reg51.h>
void main(void)
{
  unsigned int i;
  for (i = 0; i <= 255; i++)
  {
    P1 = (unsigned char)i;
  }
  while (1);
}
