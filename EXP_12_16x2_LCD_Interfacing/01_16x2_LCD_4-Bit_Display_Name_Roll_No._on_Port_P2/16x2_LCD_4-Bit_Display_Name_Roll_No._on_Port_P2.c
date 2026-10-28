#include <reg51.h>
#define LCD P2
sbit RS=P2^7;
sbit RW=P2^5;
sbit EN=P2^6;
void delay( unsigned char z );
void lcd_data( unsigned char y );
void cmnd ( unsigned char x );
unsigned char l,m;
void main ( void )
{
  unsigned char a[] = "Name";
  unsigned char b[] = "24B81A7700";
  unsigned char c, d;

  LCD = 0x00;
  cmnd (0x02); // 4-bit mode initialization
  cmnd (0x28); // 2 lines, 5x7 matrix in 4-bit mode
  cmnd (0x0C); // Display ON, Cursor OFF
  cmnd (0x06); // Auto-increment cursor
  cmnd (0x80); // Line 1 position

  for (c = 0; c < 4; c++)
  {
    lcd_data(a[c]);
  }

  cmnd (0xC0); // Line 2 position
  for (d = 0; d < 10; d++)
  {
    lcd_data(b[d]);
  }

  while (1); // Display statically without flickering
}
void lcd_data( unsigned char y )
{
l = y;
y = y & 0xf0;
y = y >> 4;
LCD = y;
RS = 1;
RW =0;
EN=1;
delay(10);
EN=0;

l = l & 0x0f;
LCD = l;
RS = 1;
RW =0;
EN=1;
delay(10);
EN=0;
}
void cmnd( unsigned char x )
{
m = x;
x = x & 0xf0;
LCD = x>>4;
RS = 0;
RW =0;
EN=1;
delay(10);
EN=0;

LCD = m & 0x0f;
RS = 0;
RW =0;
EN=1;
delay(10);
EN=0;
}

void delay( unsigned char z )
{
unsigned int i,j;
for ( i=0; i<z; i++)
for ( j=0; j<1275; j++);
}
