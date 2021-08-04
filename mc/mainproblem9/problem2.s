; ALP TO SEARCH FOR AN ELEMENT IN A SORTED ARRAY OF NUMBERS USING BINARY SEARCH
; Logic for BINARY SEARCH : 
; keep 3 variables : mid,high and low. if search > arr[mid], then low is mid .if search < arr[mid] then
; high is mid. else if they are equal then leave. else if none then just break
	AREA PROB1,CODE,READONLY
HIGH RN 1
MID RN 2
LOW RN 3
VAL RN 6
TEMP RN 7
;if you want to copy the array to the memory then use below code
;------------------------------------------------------
;ENTRY
;	; first we use high and low to load the array into memory, with mid as the load register
;	LDR HIGH,=ARRAY ; load ARR with the address of the thing.
;	MOV LOW,#0X40000000
;	LDR TEMP,COUNT
;	LDR VAL,SEARCH  ; the element to be seae
;INIT ; LOOP TO KEEP THE ARRAY AT 0X40000000 SO WE CAN OBSERVE IT PROPERLY. YOU CAN SKIP THIS BUT KEEP A LOOK AT WHERE ARRAY IS KEPT.
;	LDR MID,[HIGH],#4
;	STR MID,[LOW],#4
;	SUBS TEMP,#1
;	BNE INIT
;	MOV HIGH,LOW
;	MOV LOW,#0X40000000
;--------------------------------------------------------
; if you want to not copy the array, use below code instead
;-----------------------------------------------------------
ENTRY
	LDR LOW,=ARRAY
	LDR TEMP,COUNT
	ADD HIGH,LOW,TEMP,LSL #2
	LDR VAL,SEARCH
;--------------------------------------------------------------
LOOP ; BINARY SEARCH LOOP
	ADD MID,HIGH,LOW 			;|
	LSR MID,#3 ; DIVIDE BY 2	;| THESE 3 LINES ARE EQUIVALENT TO MID = ABS((HIGH + LOW) / 2)
	LSL MID,#2					;|
	LDR TEMP,[MID] ; LOAD THE MID VALUE
	CMP VAL,TEMP   ; AND COMPARE
	BEQ FINAL		; IF THEY ARE EQUAL JUST GO TO THE END AND SHOW RESULT
	ADDGE MID,#4    ; ELSE IF THE VALUE IS GREATER THEN THE MID, INCREMENT THE MID ADDRESS 
	MOVGE LOW,MID		;AND LOAD IT INTO LOW
	SUBLE MID,#4	; ELSE IF THE VALUE IS LESSER THAN THE MID, DECREMENT THE MID ADDRESS 
	MOVLE HIGH,MID		; AND LOAD IT INTO HIGH
	CMP HIGH,LOW	; IF HIGH < LOW IT MEANS THAT THE ELEMENT IS NOT IN THE ARRAY
	BMI ERROR
	BPL LOOP
FINAL 
	; DO THIS IF YOU ARE LOADING INTO MEMORY
;----------------------------------------------
;	LSR MID,#2
;	SUB MID,MID,#0X10000000
;----------------------------------------------
	; DO THIS IF YOU ARE ONLY REFERRING MEMORY
;----------------------------------------------
	LDR LOW,=ARRAY
	SUB MID,LOW
	LSR MID,#2
;----------------------------------------------
GO 	B GO
ERROR
	MOV MID,#0XFFFFFFFF
NO B NO

; ASSUME THIS IS THE AREA FROM WHERE THE PROGRAM GIVES DATA
	AREA TABLE,DATA,READONLY
ARRAY DCD 0,1,2,4,5,6,7,8,9,10
SEARCH DCD 9
COUNT DCD 10
	END
