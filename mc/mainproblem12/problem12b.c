//.C program to generate a square wave using Timer0 in the interrupt mode
// i tried this program it does not work on my system. 
# include <LPC214x.h>
# include <stdio.h>
unsigned int x = 0;
__irq void timer(void)
{
		x ^= 1;
	if (x)
		IOSET1 = 0xFFFFFFFF; // enable all in port 1
	else
		IOCLR1 = 0xFFFFFFFF; // disable all pins in port 1
	T0IR = 1; // clear timer interrupt flag
	VICVectAddr = 0; // acknowledge the interrupt and go back 
 }

int main()
{
 	IODIR1 = 0xFFFFFFFF; // complete port 1 is controlled
	T0MCR = 3; // trigger an interrupt and reset when tc == mr0
	T0MR0 =  100000;
	T0TC = 0x00;  
	T0TCR = 1;
	VICVectAddr4 = (unsigned)timer;

	VICVectCntl4 = 	(0x20 | 4); // this means the 4th bit of the vector controller , the one for timer0 is enabled
	VICIntEnable = (1 << 4);// enable interrupt requests 4. This register controls which of the 32 interrupt 
	//requests and software interrupts contribute to FIQ or IRQ
	while(1);
}

// VICVectCntl : Vector Control Registers 0-15 each control one of the 16 vectored IRQ slots. Slot 0 has the highest
//priority and slot 15 the lowes
// VICVectAddr : Vector Address Registers 0-15 hold the 
//addresses of the Interrupt Service routines (ISRs) for the 16 vectored IRQ slot
