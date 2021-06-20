;a. ALP to add the first n even numbers. Store the result in a memory location.
	AREA PROB1,CODE,READONLY
SUM RN 1
TERM RN 2
COUNT RN 3
PLACE RN 4

ENTRY
	MOV SUM,#1
	MOV TERM,#2
	MOV COUNT,#1
	MOV PLACE,#0x40000000 ; We will place whatever is obtained in term in the place register, and increment the address
						  ; as the progression goes on
LOOP	;Loop starts from here.
	STR TERM,[PLACE],#4 ; Every term we obtain (every even number) we are storing in the place address.
	ADD TERM,#2			; Increment term to the next term
	ADD SUM,TERM		
	ADD COUNT,#1
	CMP COUNT,#5		; Compare count and 5. we can change this 5 to any decimal number.
	BNE LOOP
	STR TERM,[PLACE],#4	; storing the last number in the even terms progression.
	STR SUM,[PLACE]		; storing the result after the progression.
GO B GO
	END
	