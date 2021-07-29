;b. ALP to convert BINARY CODED NUMBER (decimal, or octal or binary) to binary ie to hex.
;Note : a nibble is basically 4 bits.A 32 bit number has 4 bytes, so we split the number into
;		4 sets of 2 nibbles (4 x 2 x 4 = 32 bits).

	AREA PROG,CODE,READONLY
RADIX RN 0 ; whether the number is in decimal or octal or binary
LOWERNM RN 10 ; will hold the value of the mask that will only allow the upper 4 bits be taken. 
UPPERNM RN 11
LOWERN RN 3
UPPERN RN 4
RESULT RN 5 ; Stores the result 
NUMBYTES RN 6 
BYTE RN 2

ENTRY
	MOV RADIX,#10 ; TO SIGNIFY DECIMAL
	MOV LOWERNM,#0X0F
	MOV UPPERNM,#0XF0
	MOV RESULT,#0
	MOV NUMBYTES,#4
	LDR R1,=NUMBER
	ADD R1,R1,NUMBYTES
	SUB R1,R1,#1
LOOP  ; it will go 4 loops always, since 4 bytes number means 4 upper nibbles and lower nibbles.
	LDRB BYTE,[R1] ; Ldrb means it will load only a byte. register r1 will only go one byte at a loop
	SUB R1,R1,#1 ; go to the next significant byte in the number
	AND LOWERN,BYTE,LOWERNM ; the AND operation discussed above.
	AND UPPERN,BYTE,UPPERNM
	LSR UPPERN,#4			; lsr discussed above
	MLA RESULT,RADIX,RESULT,UPPERN 
	MLA RESULT,RADIX,RESULT,LOWERN
	SUBS NUMBYTES,NUMBYTES,#1 ; check if all the bytes are processed.
	BNE LOOP
STOP B STOP

NUMBER DCD 0X00003594 
	END
		;WORKING
; how the mask works: 
;	Example: the upper nibble mask is essentially 1111 0000 in binary.
; 			if a number say 23(10) will be 0010 0011 in binary. If we do AND for mask and
;			number we get	11110000 AND 00100011 = 00100000. we do lsl 4 times to this to get 
;				LSL(00100000)4 = 00000010 which is 2 in hexadecimal awell (this is stored
;					in the uppernibble register). same for the lower nibble mask and lower nibble

; MLA how it works : its basically multiply and accumulate. it takes 4 values
; eg : MLA r,m,n,a means multiply m and n , add a to the result and store in r
