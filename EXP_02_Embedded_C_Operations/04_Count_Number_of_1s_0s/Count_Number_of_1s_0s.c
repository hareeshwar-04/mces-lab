#include <reg51.h>
sbit carry = PSW^7;
void main(void)
{
  unsigned char a = 0x77;
  unsigned char i, ones = 0, zeros = 0;
  for (i = 0; i < 8; i++)
  {
    carry = a & 0x01; // Capture LSB into carry flag before shift
    a = a >> 1;
    if (carry == 1)
    {
      ones = ones + 1;
      P1 = ones;
    }
    else
    {
      zeros = zeros + 1;
      P0 = zeros;
    }
  }

  while (1);
}
