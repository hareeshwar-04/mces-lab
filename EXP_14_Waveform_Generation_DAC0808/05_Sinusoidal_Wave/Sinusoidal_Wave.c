#include <reg51.h>
#define DAC P1

void main(void)
{
  unsigned char A[] = {128, 192, 238, 255, 238, 192, 128, 64, 17, 0, 17, 64, 128};
  unsigned char i;
  while (1)
  {
    for (i = 0; i < 13; i++)
    {
      DAC = A[i];
    }
  }
}
