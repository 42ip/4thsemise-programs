	AREA PROB1,CODE,READONLY
		;ALP TO FIND nPr
; NOTE THAT FORMULA FOR nPr IS n!/(n-r)!
; so 2 factorials and one division
; note that RESULT  register serves 2 functions. one as the temporary register for multiplication operations
; and one for the final division result.
RESULT RN 1
N RN 2
R RN 3
TEMP RN 4
REG RN 5 

ENTRY
	MOV RESULT,#0
	MOV N,#10
	MOV R,#4
	SUB R,N,R
	MOV REG,N
	BL FACTORIAL
	MOV N,REG
	MOV REG,R
	BL FACTORIAL
	MOV R,REG
	BL DIVIDE
GO B GO
FACTORIAL
	MOV TEMP,REG
FACTLOOP
	SUBS TEMP,#1
	MULNE RESULT,TEMP,REG
	MOVNE REG,RESULT
	BNE FACTLOOP
	BX LR
DIVIDE
	MOV RESULT,#0
DIVLOOP
	SUBS N,R
	ADDPL RESULT,#1
	BPL DIVLOOP
	ADDNE N,R
	BX LR
	END





