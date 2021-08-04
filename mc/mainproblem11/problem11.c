#include<LPC214X.h>
//C  program  to  toggle  the  lowest  pin  of  Port  0  with  a  delay  between  the  two  states.
//Observe  and  record  the waveform  obtained  using  the  Logic Analyzerin  the  Keil simulator
void delay(void);
int main(void)
{
IODIR0 = 0x000000F0;	// Configure Ports 4 to 7 as Output port
// note that here, look at it as 0000 0000 0000 0000 0000 0000 0000 0000 (32 bits). we use hexadecimal notation
	// to indicate which bit is input and which is output. right side of any enabled bit if it is 0 then its input
	// else output. so if we take say 0x000000F0 then last two bytes we have 1111 0000 which means pins 0 to 3
	// (right to left) are input and pins 4 to 7 are output pins.
	//0101
//for sake of example, we do this
IODIR0 = 0x00000001; // meaning that we are only looking at the pin 0 (first bit) for output
while(1)
{
// uncomment below for a scenario where pins 4 and 6 get toggled along with 5 and 7 alternately
// ------------------------
//IOCLR0 =0X000000F0;
//IOSET0 =0X000000A0;	// Make all pins of Port 0 High
//delay();
//IOCLR0 =0X000000F0;
//IOSET0 =0X00000050;
//delay();
// ---------------------
	//What is expected in lab:
//---------------------------
IOSET0 = 0x00000001; // toggle pin 0 to high
delay();
IOCLR0 = 0x00000001; // toggle pin 0 to low basically clear the value in pin 0
delay();
//-------------------------
}
}
void delay(void)
{
int i = 3000;
for(int j = 0; j < i;j++);
}
