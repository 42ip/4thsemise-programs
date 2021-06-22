;ALP to find the arithmetic progression with a=3, d=7
;Note that in the program we have to create a table and store the progression in it.. that is the difference
		AREA PROB1,CODE,READONLY

TERM RN 1
COUNT RN 2
PLACE RN 3

ENTRY
	MOV TERM,#3
	MOV COUNT,#5
	LDR PLACE,=TABLE ; store the table address in place.
	STR TERM,[PLACE]
	SUB COUNT,#1
LOOP
	ADD TERM,#7
	STR TERM,[PLACE,#4]! ; use autoindexing to increment the place value by one word when the store happens
	SUBS COUNT,#1 ; The use of s after sub here means we are asking the system to update the status flags 
				  ; ( the z,c,v,n flags basically).we could use cmp also,this is another way to do it.
	BNE LOOP
GO B GO
		AREA PROGRESSION,DATA,READWRITE ; declaring the code area for our table
TABLE SPACE 10 ; CREATE A TABLE OF 10 word lengths (32 * 10 bits). WE STORE THE WORDS HERE
	END
	
