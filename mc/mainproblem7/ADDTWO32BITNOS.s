;Assembly program to add 2 32 bit numbers 
; 
	AREA PROG,CODE,READONLY
LOC1 RN 0
LOC2 RN 1
VAL1 RN 2
VAL2 RN 3
ENTRY 
	LDR LOC1,=VALUE1
	LDR LOC2,=VALUE2
	LDR VAL1,[LOC1]
	LDR VAL2,[LOC2]
	ADD R4,VAL1,VAL2
; Note that Q = Quad word (64 bits), D = Double word (32 bits),B = Byte (8 bits), W = Word(16 bits here)
VALUE1 DCQ &BBBBBBBB1 ; this is a 64 bit number : 16 digits(it should be padded with 0s on the right),
					  ;each of 4 bits = 32 
VALUE2 DCD &AAAAAAAA
	END