#include <reg51.h>
void main(void)
{
  TMOD = 0x20;
  SCON = 0x50;
  TR1 = 1;
  SBUF = 'E';
  while (TI == 0);
  TI = 0;
}
