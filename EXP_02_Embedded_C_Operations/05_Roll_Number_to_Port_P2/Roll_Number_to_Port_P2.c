#include <reg51.h>
void main(void)
{
  unsigned char x[] = "24B81A7700";
  unsigned char i;
  unsigned int d;
  while (1)
  {
    for (i = 0; i < 10; i++)
    {
      P2 = x[i];
      for (d = 0; d < 30000; d++); // delay to observe output
    }
  }
}
