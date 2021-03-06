; ALP TO SORT AN ARRAY OF NUMBERS USING BUBBLE SORT
; Logic for bubble sort : 
; compare each arr[i] and arr[i + 1] while i tends to n and n tends to 0
	AREA PROB1,CODE,READONLY
ARR RN 1
COUNT RN 2
CURR RN 3
NEXT RN 4
RES RN 7
ENTRY
	LDR ARR,=ARRAY ; load ARR with the address of the thing.
	MOV RES,#0X40000000
	MOV COUNT,#0
INIT
	LDR CURR,[ARR],#4
	STR CURR,[RES],#4
	ADD COUNT,#1
	CMP COUNT,#21
	BNE INIT
	MOV ARR,#0X40000000
LOOP
	MOV RES,#0
	SUBS COUNT,#1
	CMP COUNT,#0
	BLNE INNERLOOP
	MOV ARR,#0X40000000
	CMP COUNT,#0
	BNE LOOP
	B STOP
INNERLOOP
	LDR CURR,[ARR]
	LDR NEXT,[ARR,#4]
	CMP CURR,NEXT ; IF NEXT IS LESSER THAN CURR THE NEGATIVE FLAG WILL GET SET
	STRPL CURR,[ARR,#4]
	STRPL NEXT,[ARR]
	ADD RES,#1
	ADD ARR,#4
	CMP COUNT,RES
	BNE INNERLOOP
	BX LR
STOP B STOP
ARRAY DCD 9,8,6,5,3,234,6,34,2,34,5,34,6,2,4,5,7,34,34,56,345,56
	END