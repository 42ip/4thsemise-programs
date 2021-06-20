;ALP to compute sum of 5 terms of an arithmetic progression. First term is 3, common 
;difference is 7. Store sum in register
	AREA PROB3,CODE,READONLY
SUM RN 1
TERM RN 2
COUNT RN 3

ENTRY
	MOV SUM,#3
	MOV TERM,#3
	MOV COUNT,#1
LOOP
	ADD TERM,#7
	ADD SUM,SUM,TERM
	ADD COUNT,#1
	CMP COUNT,#5
	BNE LOOP
GO B GO
	END

	
	