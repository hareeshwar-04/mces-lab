#include <reg51.h>
#define LCD P1
sbit rowa=P2^0;
sbit rowb=P2^1;
sbit rowc=P2^2;
sbit rowd=P2^3;
sbit c0=P2^4;
sbit c1=P2^5;
sbit c2=P2^6;
sbit c3=P2^7;
sbit RS=P1^7;
sbit RW=P1^5;
sbit EN=P1^6;
void cmnd(unsigned char x);
void lcddata(unsigned char y);
void delay(unsigned int z);
unsigned char l,m;
void READ_SWITCHES(void);
void main(void)
{
P1=0x00;
P2=0xf0;
while(1)
{
unsigned char a;
unsigned char b[]="EVL KEYPAD";
		cmnd (0x02); //4-bit mode
    cmnd (0x28); //initialization of 16x2 lcd in 4bit mode
    cmnd (0x0C); //display ON cursor OFF
    cmnd (0x06); //auto increment cursor
    cmnd (0x80); //cursor at home position
for(a=0;a<10;a++)
{
lcddata(b[a]);
}
cmnd(0xc0);   //second line
while(1)
{
READ_SWITCHES();
}
}
}
void READ_SWITCHES(void)
{
rowa=0;rowb=1;rowc=1;rowd=1;
if(c0==0)
{delay(20);while(c0==0);lcddata('0');}
if(c1==0)
{delay(20);while(c1==0);lcddata('4');}
if(c2==0)
{delay(20);while(c2==0);lcddata('8');}
if(c3==0)
{delay(20);while(c3==0);lcddata('C');}
rowa=1;rowb=0;rowc=1;rowd=1;
if(c0==0)
{delay(20);while(c0==0);lcddata('1');}
if(c1==0)
{delay(20);while(c1==0);lcddata('5');}
if(c2==0)
{delay(20);while(c2==0);lcddata('9');}
if(c3==0)
{delay(20);while(c3==0);lcddata('D');}
rowa=1;rowb=1;rowc=0;rowd=1;
if(c0==0)
{delay(20);while(c0==0);lcddata('2');}
if(c1==0)
{delay(20);while(c1==0);lcddata('6');}
if(c2==0){delay(20);while(c2==0);lcddata('A');}

 if(c3==0)
{delay(20);while(c3==0);lcddata('E');}
rowa=1;rowb=1;rowc=1;rowd=0;
if(c0==0)
{delay(20);while(c0==0);lcddata('3');}
if(c1==0)
{delay(20);while(c1==0);lcddata('7');}
if(c2==0)
{delay(20);while(c2==0);lcddata('B');}
if(c3==0)
{delay(20);while(c3==0);lcddata('F');}
}
void lcddata(unsigned char y)
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
LCD= x>>4;
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

void delay(unsigned int x)
{
    unsigned int i,j;
    for(i=0;i<x;i++)
    {
       for(j=0;j<1275;j++);
    }
}
