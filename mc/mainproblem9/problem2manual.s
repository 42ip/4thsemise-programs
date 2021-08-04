
;source - https://github.com/joeskan/BinarySearch-ARM/blob/master/BinarySearch.s
; AUTHOR: JOSEPH KANG
; INSTRUCTOR: DONALD EVANS
; PROGRAM NAME: program6.s
; PURPOSE: TO COMBINE BINARY SEARCH AND PASSING BY REFERENCE TO SEARCH THROUGH A ONE DIMENSIONAL ARRAY

	AREA Program6, CODE, READONLY
	ENTRY
	
SRAM_BASE	EQU	0x40000000
	LDR	sp, =SRAM_BASE
	LDR r3, =SRAM_BASE + 200
	

	
;REGISTERS THAT WILL BE USED THROUGHOUT THE CODE
;	R1 = FIRST
;	R2 = LAST
;	R3 = MIDDLE
;	R4 = SIZE OF ENTRIES
;	R5 = THE KEY
;	R6 = ADDRESS OF THE LIST
;	R7 = TEMPORARY
	


NUM		EQU	11
SIZE	EQU	1

	ADR r6, array
	MOV r1, #0 ; lb
	MOV r2, #NUM - 1 ; ub
	MOV r5, #17 ; <================ Enter desired search value here
	STMDB r3!, {r6,r1,r2,r5, r0}
	
	
	
main 
	BL recursiveBinarySearch
	B main

	
recursiveBinarySearch
	STMDB sp!, {r4,r7,r8,r9,r10,r11,r12,lr} ; preserving all the registers we have to work with other than the four that were passed by reference
	LDMFD r3!, {r11,r7,r8,r10, r0} ; r7 = r1, r8 = r2, r10 = r5, r11 = r6
	CMP r7, r8 ; r1 > r2?
	BGT stop
	
	ADD r9, r7, r8 ; first + last
	MOV r9, r9, ASR #1 ; (first + last) / 2
	LDR r12, [r11, r9,LSL #2]; load the entry
	ADD r11, r9, LSL #2
	MOV r0, r11 ; keep this address ( r11 will be reset later )
	ADD r4, r9, LSL #1 ; r4 = scratch
	CMP r12, r10 ; a[half] > value ?
	SUBGT r8, r9, #1 ; ub = half - 1
	ADDLE r7, r9, #1 ; lb = half + 1
	LDR r11, [r3, #-4] ; reset r11
	STMFD r3!, {r11,r7,r8,r10, r0} ; main registers we're using
	LDMIA sp!, {r4,r7,r8,r9,r10,r11,r12,pc} ; preserve
	
; For some reason, the above command will not load the proper value held in LR to PC no matter how many times I tried
; 	messing around with the code. Hence, the below code.

	MOV pc, lr
	
stop
	B stop
	
array DCD 3,6,8,12,17,22,45,67,99,2089,30001
	
	END
 
;END OF CODE