;b. ALP to find the average of ten 16-bit numbers stored in memory.
	AREA PROG2,CODE,READONLY
SUM RN 1
NUM RN 2
COUNT RN 3
PLACE RN 4
AVERAGE RN 5

ENTRY
	MOV SUM,#0
	MOV COUNT,#10
	LDR PLACE,=TABLE
ADDLOOP
	LDRH NUM,[PLACE],#2
	ADD SUM,NUM
	SUBS COUNT,#1
	BNE ADDLOOP
DIVLOOP
	SUBS SUM,#10
	ADDPL AVERAGE,#1
	BPL DIVLOOP
	ADDNE SUM,#10
GO B GO

TABLE DCW 1000,2564,8936,344,5667,908,786,654,9871,456
		END