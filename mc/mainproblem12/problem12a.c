# include <LPC214x.h>
//C program to generate an asymmetric square wave of 120Hz and having a 
//duty cycle of 25% using the Timer0 module
//https://www.youtube.com/watch?v=HN5cep_EY6U&lc=UgwFd_iEBWY3FcE2sOl4AaABAg for how to use logic analyser for this problem
#define ON 25000 
#define OFF  75000
// if you are using the provided values make ON 31093  and off 93280. but keep in mind for the OFF delay, 
// T0PR , if it is 1 then half of OFF.
void delay(int clocks);
int main()
{
IODIR0 = 1 << 16 ; // means selecting pin 16 for output	
	while(1){
		IOSET0 = 1 << 16; // enabling pin 16
		delay(ON);
		IOCLR0 = 1 << 16; // clearing the value on pin 16
		delay(OFF);
	}

}

void delay(int clocks)
{
	// T0(zero)MR0(zero) : This register is used to control the functions of the Timer0.
				//Enable and reset operations of the Timer0 register can be controlled by this register.
T0MR0 = clocks;		// Load calculated count for desired delay	
T0PR = 0; 
T0MCR = 1 << 2; // meaning MCR is set to bit 2. so stop incrementing the counter when TC == MR0 (read below)
T0TCR=1;			// Enable Timer by setting bit 1 in the Timer Control Register.
while(T0TC!=T0MR0);	// wait until TC reaches the desired delay in MR0
T0TC=0;
T0TCR = 2;	// Reset Timer on the next positive edge of cycle.
	
}
// How it works : 
// Duty cycle is the fraction of a period in which a signal is active. so here, our aim is to keep the pin on 
// 25% of the cycle.
// we are going to feed the timer a value x so that it will wait for x amount according to the wave 
// calculation :
//its assymetric because 25% of the time the wave is on else it is off. so no symmetricity
// since the wave must be 120hz,ie one cycle is of 0.0083 seconds. yes
// we have cpu frequency of the lpc2148 chip  = 12 megahertz. (find it by looking at the options for target menu
// and looking at the Xtal option) so one cycle takes 0.05 x 10^-6 seconds to happen
// we need a delay of 0.0083 seconds. so question is how many cycles for the lpc chip do we wait?
// if pr = 0, and delay required = 0.0083 seconds, and the clock freq = 12 mhz, then 
// clock cycles = 0.0083 / ((1+0) / 12mhz) = 100000 clock ticks. (the 0 is for the PR value. we keep it zero for
// our case.)
// so 25 % of 100000 = 25000 = 61A8 in hex
// 75 % of 100000 = 75000 = 124F8 in hex


	// How a clock works in these systems : 
	// we have A prescale register PR, a prescale counter register PC, a timer counter TC 
 // a timer control register TCR, a count control register CTCR and a match control register MCR, which has MR0,MR1 and so on in it.
// A value is kept in the PR, say n. at every clock cycle , the value in the PC increments, up to n
// when it reaches n, the PC will be reset to zero and the TCounter register is incremented by one.
// the TCounter will keep incrementing as the timer goes on, until either an interrupt causes it to be reset, or 
// it reaches maximum 0xFFFFFFF value after which it will go back to 0.  	
//  in The MCR we set its value to 4 which means we want the timer to stop counting when TC reaches the MR value 
// we assign to it. it will also stop TC and PC. MCR has other modes aswell.

// Note that The T0MCR is 32 bit and has multiple MRs in it. the first 3 bits are for MR0. then MR1 and so on
///									000 000 000 000 000 000 000 000 000 -- if this is the bit representation of MCR
///									                    MR3 MR2 MR1 MR0 -- this is how the MRs are represented.
/// Depending on each bit, certain function is given by each MR.
//eg : 
//  first bit active : bit 0 : Interrupt on MR0 i.e trigger an interrupt when MR0 matches TC. 
  //                           Interrupts are enabled when set to 1 and disabled when set to 0.
	// second bit active : bit 1 : Reset on MR0. When set to 1 ,
//																	TC will be reset when it matched MR0. Disabled when set to 0.
// Third bit active : bit 2 :  Stop on MR0. When set to 1 , TC & PC will stop when MR0 matches TC. (we use this here.)
// the same works on bit 3.....31 but for the other MRs.

// Timer Control Register : 
// The timer control register can be used by changing the value This register is used to enable ,
  //disable and reset TC. When bit0 is 1 timer is enabled and when 0 it is disabled. 
	//When bit1 is set to 1 TC and PC are set to zero together in sync on the next positive edge of PCLK.
  //Rest of the bits of TCR are reserved.

	
