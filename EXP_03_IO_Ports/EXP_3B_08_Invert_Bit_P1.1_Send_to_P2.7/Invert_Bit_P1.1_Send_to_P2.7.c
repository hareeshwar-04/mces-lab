#include <reg51.h>
sbit a = P1^1;
sbit b = P2^7;
void main(void)
{
  a = 1; // Set P1.1 as input
  while (1)
  {
    b = ~a;
  }
}
