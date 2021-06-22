;ALP to find the sum of cubes of the first n natural numbers

; The sum of first n cubes is given by : (n(n+1))^2
;										 (   2  )
	AREA PROG2,CODE,READONLY

N RN 1
NPLUS1 RN 2
SUM RN 3
TEMP RN 4
PLACE RN 5

ENTRY
	MOV PLACE,#0X40000000 ; we will store the result in r5
	MOV N,#5
	ADD NPLUS1,N,#1
	MUL TEMP,N,NPLUS1 ; n * n + 1
	LSR TEMP,#1 ; this is equivalent to dividing temp by 2 and storing that value in temp
	MUL SUM,TEMP,TEMP ; squaring the value of temp
	STR SUM,[PLACE]
GO B GO
	END
