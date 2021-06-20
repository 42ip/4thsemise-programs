;ALP to compute sum of squares of 5 numbers starting from 1. Write and use 
;procedure SQU. Store sum in register

	AREA PROB4,CODE,READONLY
SUM RN 1
TERM RN 2
SQUARED RN 3

ENTRY
	MOV SUM,#1
	MOV TERM,#1
LOOP
	ADD TERM,#1
	BL SQU				;bl stands for branch link. we are branching out to the squ subroutine.
	ADD SUM,SQUARED,SUM
	CMP TERM,#5
	BNE LOOP
GO B GO

SQU							;here we are defining a subroutine squ(square). we call this with the bl keyword
	MUL SQUARED,TERM,TERM
	MOV PC,LR ; this is very important in subroutines. we need to put the contents of link register back in pc or we wont
			  ;	come back to the part of execution we were at before the branch takes place
			  ;PC = program counter, LR = link register
	END

	
	